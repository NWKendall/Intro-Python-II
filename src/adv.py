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
player = Player("", "", "", 100)

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

player.name = input("Welcome hero, what is your name? ")
while player.hp > 0:

    start_game = input(f"If the perils become to much, you can escape by pressing 'Q'. Are you ready to begin {player.name}? (y/q) ")
    if start_game.lower().strip() == "q":
        print("See you soon!")
        break

    player.current_room = room['outside']
    print(f"You find yourself",player.current_room,"...")
    directionInput = input("You can move by pressing 'N', 'S', 'E', 'W' to navigate. Enter the cave when you're ready...")
   
   
    try:
        if directionInput.lower().strip() == "q":
            print("CHICKEN!")
            break
        elif directionInput.lower().strip() != "n":
            print("So inert on the looming cave, you forgot about the type rope you were walking and fell to a grizzly death")
            player.hp = 0
            break
        # navigate to foyer ✅
        elif directionInput.lower().strip() == "n":
            print(f"**{player.name} walked north...**")
            print(f"You find yourself in the {player.current_room.n_to}...")
            player.current_room = room['foyer']
            directionInput = input("Which way?")

            try:

                # navigate to overlook
                if directionInput.lower().strip() != "n":
                    print("So inert on the looming cave, you forgot about the type rope you were walking and fell to a grizzly death")
                    player.hp = 0
                    directionInput = input("Which way?")
                    
        # navigate to narrow ✅
        elif directionInput.lower().strip() == "e":
            print(f"**{player.name} walked east...**")
            print(f"You find yourself in the {player.current_room.e_to}...")
            player.current_room = player.current_room.e_to
            directionInput = input("Which way?")
        # navigate to outside
        elif directionInput.lower().strip() == "s":
            print(f"**{player.name} walked south...**")
            print(f"You find yourself in the {player.current_room.s_to}...")
            player.current_room = player.current_room.s_to
            directionInput = input("Which way?")

    except ValueError:
        print("asdas")
