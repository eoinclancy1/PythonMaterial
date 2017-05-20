#based on https://github.com/mseyne/python-game/blob/master/breakout-tkinter.py

#Libraries
from Tkinter import *
import random
import sys

# data structures
COLOURS = ['white', 'tomato', 'sandy brown', 'goldenrod', 'gold', 'yellow green', 'cadet blue'] # used to get random colours for bricks

WIDTH, HEIGHT = 400, 600    # Game canvas size

# variables
numBrk = 30
bricks = []
brickDict = {} # bricks dictionary with co-ords


#Note: top left of canvas is (0,0)
bx, by, br = 200, 563, 8    # ball co-ords and radius
dx, dy = 2, -2              # ball directions, moving +45deg at start
px, py = 200, 580           # x, y rectangle co-ords, represents middle of rectangle at start
pw, ph = 80/2, 16/2         # half width and height of paddle

flag = "stop"   #game stopped on initialisation

#functions
def newGame():
    global flag, px, bx, by
    flag = "play"
    px = 200            # need to reposition ball and paddle
    bx, by = 200, 554
    lives_left.set(3)   # reset lives and score
    player_score.set(0)
    gameScreen.coords(paddle, px+pw, py+ph, px-pw, py-ph)
    gameScreen.coords(ball)
    createBricks()      #create the bricks
    ballMovement()

def setGrid(): # grid used to manage buttons at bottom of game
    gameScreen.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky=(N,W,E,S)) #setting up the grid
    btNew.grid(row=2, column=0, padx=5, pady=10)
    btPausePlay.grid(row=2, column=1)
    btContinue.grid(row=2, column=2)
    btQuit.grid(row=2, column=3)
    scoreText.grid(row=1, column=0, sticky=E)
    score.grid(row=1, column=1, sticky=W)
    livesText.grid(row=1, column=2, sticky=E)
    lives.grid(row=1, column=3, sticky=W)
    

def configureWindow():  # used to position the window
    root.title("Breakout Game using Tkinter")
    root.update_idletasks()                             # waits until all idle tasks are complete
    width = root.winfo_width()                          #returns width of the widget
    height = root.winfo_height()                        #returns height of the widget
    x = (root.winfo_screenwidth()//2) - width//2        #returns width of screen in num pixels, // means floor division
                                                        #get screen size/2 = half way in screen, minus half width of GUI means GUI centred about '0' on x-axis
    y = (root.winfo_screenheight()//2) - height//2      # same as above, will display the game in the middle of the screen
    root.geometry("{}x{}+{}+{}".format(width, height, x, y)) #used for placement of the GUI



def paddleMovement(direction):  #handles right and left arrow presses
    "Get direction from left or right key press"
    global px

    if flag == "play":
        if direction == "right":
            if px+pw == 400:
                px +=1
            elif px+pw < 400:
                px += 10
        elif direction == "left":
            if px+pw == 401:
                px -= 1
            elif px-pw > 0:
                px -= 10

        gameScreen.coords(paddle, px+pw, py+ph, px-pw, py-ph)
    else:
        pass # no arrow pressed


def ballMovement(): #handle the ball moving
    "Determine the direction the ball should move"
    global bx, by, dx, dy   # need access to the ball and direction vars

    if flag == "play": # 3 movement changes: paddle, wall and brick

        #Ball hits wall
        if bx+br >= WIDTH or bx-br <= 0:    # ball hits side wall
            dx = -dx                        # reverse x direction

        if by+br >= HEIGHT:                 # paddle misses ball
            num_lives = lives_left.get()    # decrement lives
            num_lives -= 1
            lives_left.set(num_lives)
            stopGame()
        elif by-br <= 0:                    # ball hits top wall
            dy = -dy
            

        #Ball hits brick
        if by-br <= 250:     # range where bricks exist
            if checkBrickTopBottomImpact():     
                dy = -dy                        # reverse y direction
                new_score = player_score.get()  # increment score
                new_score += 1
                player_score.set(new_score)  
            if checkBrickSideImpact():
                dx = -dx                        # reverse x direction
                new_score = player_score.get()  # increment score
                new_score += 1
                player_score.set(new_score)  

        #Ball hits paddle
        if by+br == py-ph:                  # hits top of paddle line extended in game
            if checkPaddleImpact():
                dy = - dy

        #Always
        bx += dx    # adjust ball position
        by += dy
        gameScreen.coords(ball, bx+br, by+br, bx-br, by-br) # update ball co-ords
        gameScreen.after(20, ballMovement)                  # call ballMovement function every 20ms

    else:
         pass

def createBricks(): # add bricks to the game environment
    "create bricks and store them in a list"
    w, h = 60, 20                   # size of one brick
    x, y, hw, hh = 0, 0, w/2, h/2   # co-ords centred around knowing the centre of the rectangle/brick
    count = 0
    colIndex = 0                    # colour index
    colour = COLOURS[colIndex]

    #need to empty list and dictionary if they already contain bricks
    while bricks:
        for brick in bricks: 
            gameScreen.delete(brick)    # remove from screen
            bricks.remove(brick)        # remove from list
            brickDict.pop(brick, None)  # remove from dictionary

    
    while count < numBrk:
        x += 71             # Distance between centres of blocks
        if count%5 == 0:    # Completed a row, update colours, position etc
            colIndex += 1
            colour = COLOURS[colIndex]
            x = 60
            y += 40         # filling the rows in downwards direction
        
        brick = gameScreen.create_rectangle(x-hw, y-hh, x+hw, y+hh, fill=colour)
        bricks.append(brick)
        brickDict[brick] = [x-hw, y-hh, x+hw, y+hh] # store all outside edge co-ords of brick

        count += 1
        

def checkBrickTopBottomImpact():
    "return true if ball hits brick top/bottom (Brick also removed from list and dictionary)"

    #check for ball-brick collision
    for brick in bricks:                             #loops over all bricks still in game
        
        #check if ball top hit brick bottom (fourth element in dictionary y+hh)
            # and ball centred directly below the brick ( allow for ball edges to be enough ) 
        if (by-br) == brickDict[brick][3] and (bx+br) >= brickDict[brick][0] and (bx-br) <= brickDict[brick][2]:
            print("Hit bottom of brick!!", brick)
            gameScreen.delete(brick)    # remove from screen
            bricks.remove(brick)        # remove from list
            brickDict.pop(brick, None)  # remove from dictionary
            return True                 # Brick successfully hit

        #check if ball bottom hit brick top (second element in dictionary y-hh)
            # and ball centred directly above the brick ( allow for ball edges to be enough ) 
        if (by+br) == brickDict[brick][1] and (bx+br) >= brickDict[brick][0] and (bx-br) <= brickDict[brick][2]:
            print("Hit top of brick!!", brick)
            gameScreen.delete(brick)    # remove from screen
            bricks.remove(brick)        # remove from list
            brickDict.pop(brick, None)  # remove from dictionary
            return True                 # Brick successfully hit

    return False


def checkBrickSideImpact():
    "return true if ball hits brick (Brick also removed from list and dictionary)"

    #check for ball-brick collision
    for brick in bricks:                             #loops over all bricks still in game

        #check if ball rhs hit brick lhs (first element in dictionary x-hw)
            # and ball centred at side of brick ( allow for ball edges to be enough )
        if (bx+br) == brickDict[brick][0] and (by+br) >= brickDict[brick][1] and (by-br) <= brickDict[brick][3]:
            print("Hit LHS of brick!!", brick)
            gameScreen.delete(brick)    # remove from screen
            bricks.remove(brick)        # remove from list
            brickDict.pop(brick, None)  # remove from dictionary
            return True                 # Brick successfully hit

        #check if ball lhs hit brick rhs (third element in dictionary x+hw)
            # and ball centred at side of brick ( allow for ball edges to be enough )
        if (bx-br) == brickDict[brick][2] and (by+br) >= brickDict[brick][1] and (by-br) <= brickDict[brick][3]:
            print("Hit RHS of brick!!", brick)
            gameScreen.delete(brick)    # remove from screen
            bricks.remove(brick)        # remove from list
            brickDict.pop(brick, None)  # remove from dictionary
            return True                 # Brick successfully hit

    return False


def checkPaddleImpact(): # check if ball collided with paddle
    "Check if ball hit top  of paddle"
    pxMax = px+(80/2)                       # calculate the extents of the paddle
    pxMin = px-(80/2)
    if bx >= pxMin and bx <= pxMax:         # check for ball in paddle range
        print("Hit Paddle!", pxMax, pxMin)
        return True

def checkBricks():
    "check coords of each brick"
    print(bricks)       # print the list
    print(brickDict)    # print the dictionary
    c = 0

    while c < len(bricks):
        print(bricks[c])
        print(gameScreen.coords(bricks[c]))
        print(brickDict[bricks[c]][0])
        print(brickDict[bricks[c]][1])
        print(brickDict[bricks[c]][2])
        print(brickDict[bricks[c]][3])
        c+=1

def PausePlayGame():    # user can pause/play game as required
    global flag
    if flag == "play":
        flag = "stop"
    else:
        flag = "play"
        ballMovement()

def stopGame():         # stops current game execution - used when paddle misses ball
    global flag
    flag = "stop"

def continueGame():     # called to use another life 
    global flag
    global flag, px, bx, by
    flag = "play"
    px = 200            #need to reposition ball and paddle
    bx, by = 200, 554
    if lives_left.get() == 0:   # all lives lost
        stopGame()              
        newGame()               # reset the game
    else:       # lives left
        gameScreen.coords(paddle, px+pw, py+ph, px-pw, py-ph)   # reposition paddle
        gameScreen.coords(ball) # reposition ball   
        ballMovement()  # set ball moving

def exit(event):
    sys.exit()
    
                    

if __name__ == "__main__":
    print "main method called"
    root = Tk()
    root.bind("<Escape>", exit)

    #create the cavnas for the main screen
    gameScreen = Canvas(root, width=WIDTH, height=HEIGHT)

    #create the buttons to control the game
    btQuit = Button(root, text="Quit", command = root.destroy)
    btPausePlay = Button(root, text="Pause/Play", command = PausePlayGame)
    btContinue = Button(root, text="Continue", command = continueGame)
    btNew = Button(root, text="New Game", command = newGame)

    #create labels for the score and lives
    player_score = IntVar()
    lives_left = IntVar()
    
    scoreText = Label(root, text="Score: ")
    score = Label(root, textvariable = player_score)
    livesText = Label(root, text="Lives Left: ")
    lives = Label(root, textvariable = lives_left)

    #create a rectangle to use as the paddle and bind the arrow keys to it for control
    paddle = gameScreen.create_rectangle(px+pw, py+ph, px-pw, py-ph, fill="dodger blue", width=0)

    gameScreen.bind("<Right>", lambda e: paddleMovement("right")) # setup action for right arrow press
    gameScreen.bind("<Left>", lambda e: paddleMovement("left")) # setup action for left arrow press
    gameScreen.focus_set() # set the focus back to screen

    #create a circle to use as the ball
    ball = gameScreen.create_oval(bx+br, by+br, bx-br, by-br, fill="tomato", outline="firebrick")

    #create the bricks
    createBricks()

    #check the bricks
    setGrid()
    configureWindow()

    #loop the interface
    root.mainloop()
    

    
