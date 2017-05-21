#!/usr/bin/env python2

#Above gives the path to the python interpreter

#Collection of small games

from Tkinter import *   # used to create a simple graphical interface
                        # this means of importing avoid having to use Tkinter. (whatever)

         # import the small games developed
import rpsModified
import pokerDice
import hangman 

root = Tk() # create a graphical window
root.title("Microgame Collection") # title of the window

mainframe = Frame(root, height = 200, width = 500) # creating a frame within the window, set min height and width
mainframe.pack_propagate(0) # used to create the window and make sure its the size defined
mainframe.pack(padx = 5, pady = 5) # add padding around the frame

intro = Label(mainframe, text = """Linux User & Developers Mega Microgames Collection.
Please select one of the following games to play""") # resides in main frame, triple quotes to allow it go over multiple lines
intro.pack(side = TOP) # display it and tell Tkinter to put at top of interface

rps_button = Button(mainframe, text = "Rock, Paper, Scissors", command = rpsModified.gui) # calls the gui function
rps_button.pack() # place it in the window

hm_button = Button(mainframe, text = "Hangman", command = hangman.start) # runs in command line
hm_button.pack()

pd_button = Button(mainframe, text = "Poker Dice", command = pokerDice.start)
pd_button.pack()

exit_button = Button(mainframe, text = "Quit", command = root.destroy) # ends loop started with root.mainloop()
exit_button.pack(side = BOTTOM)

root.mainloop() # allows the main window to continue to work and be updated without exiting the program unless specified


