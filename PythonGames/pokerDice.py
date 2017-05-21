#!/usr/bin/env python2

import random
from itertools import groupby

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = { nine : "9", ten : "10", jack : "J", queen : "Q", king : "K", ace : "A"}

player_score = 0
comp_score = 0
player_result = 10
comp_result = 10

def start():
    print "Welcome to the poker dice game!"
    while game():
        pass
    scores()


def game():
    print "You will now roll 5 dice"
    throws()
    return play_again()

def throws():
    roll_number = 5
    dice = roll(roll_number)
    dice.sort()
    for i in range(len(dice)):
        print "Dice ", i+1, " : ", names[dice[i]]

    result = hand(dice)
    print "You currently have ", result

    while True:
        rerolls = raw_input("How many die do you want to throw again?  ")
        try:
            rerolls = int(rerolls)
            if rerolls in (0,1,2,3,4,5):
                break
        except ValueError:
            pass
        print "Please enter a number in the range 0-5: "

    if rerolls == 0:
        print "Your final hand is ", result

    else:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = range(rerolls)   # used to store the specific dice to be rerolled
        print "Enter the number of a dice to reroll: "
        iter = 0
        while iter < rerolls:
            iter += 1
            while True:
                selection = input("")
                try:
                    if selection in (1,2,3,4,5):
                        break
                except ValueError:
                    pass
                print "Please enter either 1, 2, 3, 4 or 5"
            dice_changes[iter-1] = selection-1
            print "You have changed dice ", selection

        iter = 0
        while iter < rerolls:
            iter += 1
            replacement = dice_rerolls[iter-1]          # a new value
            dice[dice_changes[iter-1]] = replacement    # place new value in index of dice to be replaced

        dice.sort() # order the die based on value
        for i in range(len(dice)):
            print "Dice ", i , " : ", names[dice[i]]

        result = hand(dice)
        print "Your final hand is ", result


    print "The computer hand is......"
    roll_number = 5
    comp_dice = roll(roll_number)
    for i in range(len(comp_dice)):
        print "Dice ", i+1, " : ", names[comp_dice[i]]

    result = hand(comp_dice)
    print "Computer currently has ", result

    declare_winner(dice, comp_dice)

def roll(roll_number):
    poss_numbers = range (1,7) # values 1 to 6
    dice = range(roll_number)
    iter = 0
    while iter < roll_number:
        dice[iter] = random.choice(poss_numbers)
        iter += 1
    return dice

def hand(dice): # list passed in (dice) will already have been sorted
    dice_hand = [len(list(group)) for key , group in groupby(dice)] # GroupBy counts the number of occurances of each dice face
    dice_hand.sort(reverse=True)                                    # Sort then in descending order
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice == straight1 or dice == straight2:
        return " a straight"
    elif dice_hand[0] == 5:
        return " five of a kind!"
    elif dice_hand[0] == 4:
        return " four of a kind!"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return " a full house!"
        else:
            return " three of a kind!"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return " two pair!"
        else:
            return " one pair!"
    else:
        return " a high card!"


def declare_winner(dice, comp_dice):
    global player_result, comp_result, player_score, comp_score
    player_result = handValue(dice)
    comp_result = handValue(comp_dice)
    if player_result == comp_result:
        print "Tie Game!!!"
    elif player_result > comp_result:
        print "Player Wins"
        player_score += 1
    else:
        print "Computer Wins"
        comp_score += 1
        



def handValue(dice): # list passed in (dice) will already have been sorted
    dice_hand = [len(list(group)) for key , group in groupby(dice)] # GroupBy counts the number of occurances of each dice face
    dice_hand.sort(reverse=True)                                    # Sort then in descending order
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice == straight1 or dice == straight2:
        return 10
    elif dice_hand[0] == 5:
        return 9
    elif dice_hand[0] == 4:
        return 8
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return 7
        else:
            return 6
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return 5
        else:
            return 4
    else:
        return 3



def play_again():
    answer = raw_input("Do you want to roll the dice again? [Y/n]  ")
    if answer in ("Y", "y", "yes", "Yes"):
        return answer
    else:
        print "Thanks for playing!"

def scores():
    global player_score, comp_score
    print "HIGH SCORES"
    print "Player Score: ", player_score
    print "Computer Score: ", comp_score

if __name__ == '__main__':
    start()

            
