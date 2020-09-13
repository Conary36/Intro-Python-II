import sys

from player import Player
from room import Room

from src.items.charm import Charm
from src.items.weapon import Weapon


# Declare items for rooms
lamp = Charm('lamp', 'Shining bright', 2)
sword = Weapon('sword', 'Double Edged Blade', 5)
shield = Weapon('shield', 'Defends against arrows', 10)
crucifix = Charm('crucifix', 'wards off vampires', 8)
cloak = Charm('cloak', 'For invisibility', 10)
loot = Charm('loot', 'chest full of treasure', 9)
# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons", [lamp]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [sword]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [cloak]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [shield]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [loot]),

    'dungeon': Room("Dark Dungeon", """ A trap door from the treasure Room leads to 
    a dimly lit dungeon filled skeletons chained to the wall. Something Rustles in the far corner.""", [crucifix])
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
        # User chooses direction
        player_input = input("Please choose a direction").lower().strip()
        if player_input in directions:
            player.player_move(player_input)

        elif player_input in ['i', 'holster']:
            print(player.holsterItems())
        if len((Item := player_input.split(' '))) == 2:
            action, obj = Item
        elif action == 'pick up':
            player.collectItem(f"You have just found {obj}")
        elif action == 'drop it':
            player.putDownItem(f"{obj} is dropped")
        elif player_input == 'q':
            print(f"You have fell in a ditch, Goodbye")
        else:
            print(f'Error: command "{player_input}" is invalid')
            sys.exit()


if __name__ == '__main__':
    game()
