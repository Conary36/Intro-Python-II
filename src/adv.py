import sys, os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'dungeon': Room("Dark Dungeon", """ A trap door from the treasure Room leads to 
    a dimly lit dungeon filled skeletons chained to the wall. Something Rustles in the far corner.""")
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
room['treasure'].d_to = room['dungeon']
room['dungeon'].n_to = room['treasure']

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

lamp = Item('lamp', 'Shining bright')
sword = Item('sword', 'Double Edged Blade')
shield = Item('shield', 'Defends against arrows')
crucifix = Item('crucifix', 'wards off vampires')
cloak = Item('cloak', 'For invisibility')
loot = Item('loot', 'chest full of treasure')
print("************************************\n"
      "************************************")
directions = {"n", "s", "e", "w", "d"}

room['outside'].addItem(lamp)
room['foyer'].addItem(sword)
room['foyer'].addItem(shield)
room['dungeon'].addItem(crucifix)
room['overlook'].addItem(cloak)
room['treasure'].addItem(loot)


def game():
    player_name = input('Enter your name: ')
    player = Player(player_name, room['outside'])
    print(f'{player.name} your GAME has begun')

    while player:

        print(f'You are in the {player.current_room.name}\n{player.current_room.description}')

        player_input = input("Please choose a direction").lower().strip()
        if player_input in directions:
            player.player_move(player_input)

        elif player_input in ['i', 'holster']:
            player.holsterItems()

        elif len((player_input := player_input.split(' '))) == 2:
            action, obj = player_input
            if action == 'pick up':
                player.collectItem(f"You have just found {obj}")
        elif player_input == 'drop it':
            player.putDownItem(f"{obj} is dropped")
        elif player_input == 'q':
            print(f"You have fell in a ditch, Goodbye")
            sys.exit()


game()
