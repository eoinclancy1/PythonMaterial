#!/usr/bin/env python2

# Creating a gui for the rock, paper, scissors game

from Tkinter import * # (Tk interface) imports all functions without having to call Tkinter. (whatever) later
from ttk import * # allows for arranging the GUI in a grid, easier to use
import random

def gui():
    rock = 1
    paper = 2
    scissors = 3

    names = { rock : "Rock", paper : "Paper", scissors : "Scissors" }
    rules = { rock : scissors, paper : rock, scissors: paper }

    def start():
        while game():
            pass

    def game():
        player = player_choice.get() # get the value entered by the user
        computer = random.randint(1,3)
        computer_choice.set(names[computer]) # display the randomly chosen computer hand
        result(player, computer) # get the result

    def result(player, computer):
        new_score = 0
        if player == computer:
            result_set.set("Tie Game")
        elif rules[player] == computer:
            result_set.set("Player wins!")
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)
        else:
            result_set.set("Computer Wins!")
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)

    rps_window = Toplevel() # the original window is part of the mainloop, so cannot create this window using Tk()
                            # This allows the window to run separately and on top of the main window
    rps_window.title("Rock, Paper, Scissors Game")

    # In Tkinter, must let the interface know whether the var is an int or String
    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_choice.set(1)
    player_score = IntVar()
    computer_score = IntVar()

    rps_frame = Frame(rps_window, padding = '3 3 12 12', width = 300) # padding used to give each item space
    rps_frame.grid(column=0, row=0, sticky=(N,S,E,W)) # grid used to create the frame, row and column creates r and c in the window
    rps_frame.columnconfigure(0, weight=1)            # sticky allows for justification with specific directions, row and col given same weighting (0)
    rps_frame.rowconfigure(0, weight=1)

    Label(rps_frame, text = "Player").grid(column=1, row=1, sticky=W)
    Radiobutton(rps_frame, text = 'Rock', variable = player_choice, value = 1).grid(column=1,
                                                row=2, sticky=W)
    Radiobutton(rps_frame, text = 'Paper', variable = player_choice, value = 2).grid(column=1,
                                                row=3, sticky=W)
    Radiobutton(rps_frame, text = 'Scissors', variable = player_choice, value = 3).grid(column=1,
                                                row=4, sticky=W)

    Label(rps_frame, text = 'Computer').grid(column=3, row=1, sticky=W)
    Label(rps_frame, textvariable = computer_choice).grid(column=3, row=2, sticky=W)

    Button(rps_frame, text="Play", command = start).grid(column=2, row=2)
    
    Label(rps_frame, text="Score").grid(column=1, row=5, sticky=W)
    Label(rps_frame, textvariable = player_score).grid(column=1, row=6, sticky=W)

    Label(rps_frame, text="Score").grid(column=3, row=5, sticky=W)
    Label(rps_frame, textvariable = computer_score).grid(column=3,row=6,sticky=W)

    Label(rps_frame, textvariable =result_set).grid(column = 2, row=7)

if __name__ == '__main__':
    gui()
    
    

