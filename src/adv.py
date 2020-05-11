import cmd
import textwrap
import sys
import os
import time
import random


from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


# navigation

player = Player("", room['outside'])


def prompt():
    os.system('clear')
    print("##################################")
    display(player.current_room.room_name)
    print("\n##################################")
    print("                                  ")
    print("                                  ")
    display(player.current_room.description)
    print("\n                                  ")
    print("                                  ")
    print("##################################")

    while player.hp > 0 and player.game_over is False:

        print(f"\n ===============")
        print(f"Which way?")  # rename to action chooser, choose movement or search

        user_input = input("> ")
        user_action = user_input.lower().strip()
        cardinal = ("n", "s", "e", "w", "north",
                    "south", "east", "west", "q", "quit", "exit", "h", "help" ,"?")

        if user_action not in cardinal:
            print("Not a valid direction or instruction, try again or press 'Q' to quit.\n")
            user_input = input("> ")
            user_action = user_input.lower().strip()
        if user_action in ("n", "s", "e", "w"):
            player.current_room = player.change_room(
                player.current_room, user_action)
            prompt()
            # else:
            #     player.current_room = room[player.current_room]
            #     wrong_way()
            #     prompt()
        if user_action in ("q", "quit", "exit"):
            quit()
        if user_action in ("help", "?", "h"):
            help_menu()

# helper functions


def wrong_way():
    print("Nothing lies for you that way...")
    user_input = input("> ")
    user_action = user_input.lower().strip()
    cardinal = ("n", "s", "e", "w", "q")
    if user_action in cardinal:
        prompt()
    else:
        wrong_way()


def quit():
    print("are you sure? (Y/N)\n")
    answer = input("> ")
    while len(answer.lower().strip()) > 1:
        print("Please select Y or N")
        answer = input("> ")
    if answer.lower().strip() == "y":
        print("See you next time...")
        os.system('clear')
        sys.exit()
    elif answer.lower().strip() == "n":
        prompt()


def help_menu():
    print("Type 'Play' to start the game or type 'Q' or'Quit' to Qui. use N, S, E, W to navigate")
    print("In game use 'N', 'S', 'E', 'W' to navigate and 'Enter' to confirm an action")
    


def display(text_var):
    for character in text_var:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def main_game():
    welcome()
    prompt()
        # most functionality within prompt function loc 81

# title screen & options


def title_screen():
    os.system('clear')
    print("##################################")
    print("#         Darkest Dungeon        #")
    print("##################################")
    print("                                  ")
    print("              -Play-              ")
    print("              -Help-              ")
    print("              -Quit-              ")
    print("                                  ")
    print("##################################")
    title_screen_options()


def title_screen_options():
    print("Please choose")
    option_input = input("> ")
    option = option_input.lower().strip()
    if option in ("help", "h", "?"):
        help_menu()
        title_screen_options()
    if option in ("p", "play"):
        main_game()
    if option in ("quit", "exit", "q"):
        os.system('clear')
        sys.exit()
    else:
        title_screen_options()


def welcome():
    os.system('clear')
    name_question = "Welcome hero, what is your name?"

    print("##################################")
    print("#         Darkest Dungeon        #")
    print("##################################")
    print("                                  ")
    print("                                  ")
    display(name_question)
    print("                                  ")
    print("                                  ")
    print("##################################")
    player_name = input("> ")
    player.name = player_name


# Game start
title_screen()


# change_room class method not respecting game boundaires
# while loop not recognising cardiunal variable ✅
# quit function is bugging out ✅
# in game help not working ✅
# title help and quit not working ✅

# research
# whitespace if/else
