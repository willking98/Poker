import random as rd
import tkinter as tk

#x = ["C", "D", "H", "S"]
#y = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
#z = []

#class Card:
#    def __init__(self, value, suit):
#        self.value = value
#        self.suit = suit

#suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
#values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

#deck = [Card(value, color) for value in values for color in suits]
#for card in deck:
#    print(card.value, card.suit)

#print(deck)
#print(len(deck))


#print(z)
name1 = input("Player 1 name: ")
name2 = input("Player 2 name: ")

stack1 = 100
stack2 = 100

blinds = [1, 1, 1, 2, 2, 2, 3, 3, 3]
deck = []

# Variables that must exist
p2_action2 = 0
p1_action3 = 0

for i in range(1, 53):
    deck.append(i)

for game_num in range(1, 13):
    s_blind = blinds[game_num]
    b_blind = s_blind * 2

    p1_flop = rd.sample(deck, 2)
    print(str(name1) + "'s cards: " + str(p1_flop))
    deck.remove(p1_flop[0])
    deck.remove(p1_flop[1])

    blind1 = input(name1 + " you are the small blind, press [enter] to continue: ")
    stack1 = stack1-float(s_blind)

    p2_flop = rd.sample(deck, 2)
    print(str(name2) + "'s cards: " + str(p2_flop))
    deck.remove(p2_flop[0])
    deck.remove(p2_flop[1])

    blind2 = input(name2 + " you are the big blind, press [enter] to continue: ")
    stack2 = stack2 - float(b_blind)

    balance = b_blind - s_blind
    p1_action1 = input(name1 + " do you wish to call (" + str(int(balance)) + "), fold, or raise? ")

    if p1_action1 == "call":
        p1_bet1 = 1
        stack1 = stack1-p1_bet1

    if p1_action1 == "fold":
        p1_bet1 = 0
        print(name2 + " wins hand " + str(game_num) + "!")
        input("Press enter to continue to play hand " + str(game_num+1) + "!")
        stack2 = stack2 + s_blind + b_blind
        continue

    if p1_action1 == "raise":
        p1_bet1 = input("How much do you want to raise by?" + " (min raise = " + str(blind2) + ") :")
        p1_bet1 = float(p1_bet1)
        stack1 = stack1-(p1_bet1+balance)


        p2_action1 = input(name2 + ", " + name1 + " has raised you by " + str(p1_bet1) + ", would you like to call, reraise or fold? ")

        if p2_action1 == "call":
            p2_bet1 = p1_bet1
            stack2 = stack2-p2_bet1

        if p2_action1 == "fold":
            p2_bet1 = 0
            print(name1 + " wins hand " + str(game_num) + "!")
            input("Press enter to continue to play hand " + str(game_num+1) + "!")
            stack1 = stack1 + b_blind + s_blind + p1_bet1 + balance
            continue

        if p2_action1 == "reraise":
            p2_bet1 = input("How much do you want to reraise by?" + " (min raise = " + str(p1_bet1*2) + ") :")
            # Call existing amount then reraise
            p2_bet1 = float(p2_bet1)
            stack2 = stack2-(p2_bet1+p1_bet1)

            # Action back on player 1 after reraise from player 2
            p1_action2 = input(name1 + ", " + name2 + " has reraised you by " + str(p2_bet1) + ", would you like to call, reraise or fold? ")
            if p1_action2 == "call":
                p1_bet2 = p2_bet1
                stack1 = stack1-p1_bet2

            if p1_action2 == "fold":
                p1_bet2 = 0
                print(name2 + " wins hand " + str(game_num) + "!")
                input("Press enter to continue to play hand " + str(game_num+1) + "!")
                stack2 = stack2 + b_blind*2 + p1_bet1*2 + p2_bet1
                continue

            if p1_action2 == "reraise":
                p1_bet2 = input("How much do you want to reraise by?" + " (min raise = " + str(p2_bet1*2) + ") :")
                # Call existing amount then reraise
                p1_bet2 = float(p1_bet2)
                stack1 = stack1-(p1_bet2+p2_bet1)

                # Action back on player 2 after reraise from player 1
                p2_action2 = input(name2 + ", " + name1 + " has reraised you by " + str(p1_bet2) + ", would you like to call, go all in or fold? ")

                if p2_action2 == "call":
                    p2_bet2 = p1_bet2
                    stack2 = stack2-p2_bet2

                if p2_action2 == "fold":
                    p2_bet2 = 0
                    stack1 = stack1 + b_blind*2 + p1_bet1*2 + p2_bet1*2 + p1_bet1

                if p2_action2 == "all in":
                    p2_bet2 = stack2 - p1_bet2
                    stack2 = stack2 - p2_bet2

                    # Action back on player 1 after all-in from player 2
                    p1_action3 = input(name1 + ", " + name2 + " has gone all-in! To call it will be " + str(p2_bet2) + ", would you like to call or fold? ")

                    if p1_action3 == "call":
                        p1_bet3 = p2_bet2
                        stack1 = stack1-p1_bet3

                    if p1_action3 == "fold":
                        p1_bet3 = 0
                        stack2 = stack2 + b_blind*2 + p1_bet1*2 + p2_bet1*2 + p2_bet2

    # Pre-flop betting has concluded (if both players all in just deal all cards and determine winner)
    if p2_action2 == "all in" and p1_action3 == "call":
        print("Let's see the flop!")
        flop = rd.sample(deck, 4)
        deck.remove(flop[0])
        deck.remove(flop[1])
        deck.remove(flop[2])
        deck.remove(flop[3])
        flop.remove(flop[0])
        print("The flop: " + str(flop))
        input("Press [enter] to see the turn card")
        turn = rd.sample(deck, 2)
        deck.remove(turn[0])
        deck.remove(turn[1])
        turn.remove(turn[0])
        flop.append(turn[0])
        print("The turn: " + str(flop))
        input("Press [enter] to see the river card")
        river = rd.sample(deck, 2)
        river.remove(river[0])
        flop.append(river[0])
        print("The river: " + str(flop))
        input("Time to show down. Press [enter] to continue")
        print(name1 + "'s cards: " + p1_flop)
        print(name2 + "'s cards: " + p2_flop)

    # Insert hand detection functions

        continue

    print("Let's see the flop!")
    flop = rd.sample(deck, 4)
    deck.remove(flop[0])
    deck.remove(flop[1])
    deck.remove(flop[2])
    deck.remove(flop[3])
    flop.remove(flop[0])
    print("The flop: " + str(flop))

    # Flop betting
    p1_flop_action1 = input(name1 + " the action is on you, would you like to check, bet or fold? ")

    if p1_flop_action1 == "check":
        p2_flop_action1 = input(name2 + ", " + name1 + " has checked, would you like to check, bet or fold? ")

        if p2_flop_action1 == "check":
            input("Press [enter] to see the turn card")
            turn = rd.sample(deck, 2)
            deck.remove(turn[0])
            deck.remove(turn[1])
            turn.remove(turn[0])
            flop.append(turn[0])
            print("The turn: " + str(flop))

            # Turn betting
            p1_turn_action1 = input(name1 + " the action is on you, would you like to check, bet or fold? ")
            if p1_turn_action1 == "check":
                p2_turn_action1 = input(name2 + ", " + name1 + " has checked, would you like to check, bet or fold? ")

                if p2_turn_action1 == "check":
                    input("Press [enter] to see the river card")
                    river = rd.sample(deck, 2)
                    deck.remove(river[0])
                    deck.remove(river[1])
                    river.remove(river[0])
                    flop.append(river[0])
                    print("The river: " + str(flop))

                    p1_river_action1 = input(name1 + " the action is on you, would you like to check, bet or fold? ")
                    if p1_river_action1 == "check":
                        p2_river_action1 = input(name2 + ", " + name1 + " has checked, would you like to check, bet or fold? ")
                        if p2_river_action1 == "check":
                            input("Time to show down. Press [enter] to continue")
                            print(name1 + "'s cards: " + p1_flop)
                            print(name2 + "'s cards: " + p2_flop)



                # Insert hand detection functions



    if p1_action1 == "fold":
        p1_bet1 = 0
        print(name2 + " wins hand " + str(game_num) + "!")
        input("Press enter to continue to play hand " + str(game_num+1) + "!")
        stack2 = stack2 + s_blind + b_blind
        continue

    if p1_action1 == "raise":
        p1_bet1 = input("How much do you want to raise by?" + " (min raise = " + str(blind2) + ") :")
        p1_bet1 = float(p1_bet1)
        stack1 = stack1-(p1_bet1+balance)


    input("Press [enter] to see the turn card")
    turn = rd.sample(deck, 2)
    deck.remove(turn[0])
    deck.remove(turn[1])
    turn.remove(turn[0])
    flop.append(turn[0])
    print("The turn: " + str(flop))
    input("Press [enter] to see the river card")
    river = rd.sample(deck, 2)
    river.remove(river[0])
    flop.append(river[0])
    print("The river: " + str(flop))

    if pre_flop_bet == "call" or pre_flop_bet == str(balance):
        print("Let's see the flop!")
    else:
        print(name2 + " wins game" + str(game_num) + "!")
        input("Press enter to continue to play hand " + str(game_num+1) + "!")
        continue

    flop = rd.sample(deck, 4)
    flop.remove(flop[0])
    print("The flop: ", str(flop))
