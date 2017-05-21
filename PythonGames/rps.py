#!/usr/bin/env python2
#Rock Paper Scissors Game

import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock : "Rock",
          paper : "Paper",
          scissors : "Scissors" }

rules = { rock : scissors,
          paper : rock,
          scissors : paper }

player_score = 0
comp_score = 0

def start():
    print "Now playing rock, paper, scissors!"

    while game():        # Keep playing the game - game returns 0 if finished, otherwise to continue, returns non-zero
        pass             # Used when a statement is required syntactically but do not want any command to execute
    scores()

def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again() # Probably returns 0 (*) if the user wants to exit, non-zero otherwise

def move():
    while True:
        print
        player = raw_input("Rock = 1 \nPaper = 2 \nScissors = 3\n Make a move:  ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass        # Do nothing - then repeats until valid entry
        print "Invalid value entered. Please try again with a number 1-3" 

def result(player, computer):
    print "1....."
    time.sleep(1)
    print "2....."
    time.sleep(1)
    print "3....."
    time.sleep(0.5)
    print "Player threw {0}!".format(names[player])
    print "Computer threw {0}!".format(names[computer])
    pBeats = rules[player]
    cBeats = rules[computer]
    global player_score, comp_score # Calling the scores. Allows for changing the variable and to be used outside the variable
    if player == computer:
        print "Tie Game"
    elif pBeats == computer:
        print "Player Wins!!"
        player_score += 1
    else: 
        print "Computer Wins!!"
        comp_score += 1
     
def play_again():
    answer = raw_input("\nWould you like to play again? [Y/n]   ")
    if answer in ("y", "Y", "yes", "Yes"):
            return answer
    else:
            print "\nThanks for playing!" # Probably returns 0 (*)

def scores():
    global player_score, comp_score
    print "High Scores!"
    print "Player: ", player_score
    print "Computer: ", comp_score

#allows for script to be used in 2 ways
    #1. can execute from command line
    #2. can import into another python script - won't execute the code on import
if __name__ == '__main__':
    start()
    
            
