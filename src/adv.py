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

def intro():
    print(f"##### {player.current_room.room_name} #####")
    print(f"{player.current_room.description}")
    prompt()

def prompt():
    print(f"\n ===============")
    print(f"Which way?")
    user_action = input("> ")
    cardinal = ["n", "s", "e", "w", "q"]
    while user_action.lower().strip() not in cardinal:
        print("Not a direction, try again or press 'Q' to quit.\n")
        user_action = input("> ")
    if user_action.lower().strip() == "q":
        sys.exit()
    else:
        try:
            if player.current_room.n_to and user_action.lower().strip() == "n":
                player.current_room = player.current_room.n_to
                player.explore()
                prompt()
            else:
                while user_action.lower().strip() not in cardinal:
                    print("Can't go that way!")
                    user_action = input("> ")

        
        except ValueError:
            print("asdasdasd")
    

# title screen

# creates player

# player defines name


def main_game():
    while player.hp > 0 and player.game_over is False:
        welcome()
        intro()


def welcome():
    os.system('clear')
    name_question = "Welcome hero, what is your name?"
    for character in name_question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    player.name = player_name

main_game()