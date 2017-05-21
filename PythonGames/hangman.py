#!/usr/bin/env python2

from random import *

player_score = 0
comp_score = 0

def hangedman(hangman):
    graphic = [
    """
        +----------+
        |
        |
        |
        |
        |
        |
        |
       ==============
    """,
    """
        +----------+
        |          |
        |          O
        |
        |
        |
        |
        |
       ==============
    """,
    """
        +----------+
        |          |
        |          O
        |          |
        |
        |
        |
        |
       ==============
    """,
    """
        +----------+
        |          |
        |          O
        |         -|
        |
        |
        |
        |
       ==============
    """,
    """
        +----------+
        |          |
        |          O
        |         -|-
        |
        |
        |
        |
       ==============
    """,
    """
        +----------+
        |          |
        |          O
        |         -|-
        |         /
        |
        |
        |
       ==============
    """,
    """
        +----------+
        |          |
        |          O
        |         -|-
        |         / \
        |
        |
        |
       ==============
    """]

    print graphic[hangman]
    return

def start():
    print "Loading the Linux Hangman Game"
    while game():
        pass
    scores()

def game():
    #dictionary = ["gnu", "kernal", "linux", "magenta", "penguin", "snake", "ubuntu"]
    dictionary = []
    with open('hard_words.txt', 'r') as f: # used as a context manager
        for line in f.readlines():
            word = line.strip()
            dictionary.append(word)
    
    word = choice(dictionary) #selects a random element from the list
    word_length = len(word)
    clue = word_length * ["_"] # generates word_length underscores
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_wrong = 0
    letters_right = 0
    global comp_score, player_score # must refer to the gloabal variables in this way when modifying

    hangedman(letters_wrong)
    print " ".join(clue)

    # player must have attempts remaining & check if word has not yet been found
    while (letters_wrong < tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1: # only returns -1 when not guessed already  
                print "You have previously guessed ", letter
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print "Unlucky, the word does not contain - ", letter
                else:
                    print "Well done, the word does contain ", letter
                    for i in range(word_length):
                        if letter == word[i]: # covers the case where the word contains letter duplicates, better than using first_index
                            clue[i] = letter
                            letters_right += 1
        else:
            print "Choose another letter"

        hangedman(letters_wrong)
        print " ".join(clue)
        print "Guesses so far: ", letters_tried

        if letters_wrong == tries:
            print "Game Over"
            print "The word was: ", word
            comp_score += 1
            break

        if "".join(clue) == word:
            print "You have found the word!!!!"
            print "The word was ", word
            player_score += 1
            break
    return play_again()
                    



def guess_letter():
    print
    letter = raw_input("Please enter the next letter to check:  ")
    letter.strip() # remove whitespace
    letter.lower() # convert to lower case
    print
    return letter

def play_again():
    answer = raw_input("Do you want to play again? [Y/n]  ")
    if answer in ["Y", "y", "yes", "Yes"]:
        return answer
    else:
        print "Thanks for playing!"

def scores():
    global player_score, comp_score
    print "HIGH SCORES"
    print "Player: ", player_score
    print "Computer: ", comp_score

if __name__ == "__main__":
    print "Why am I called"
    start()
