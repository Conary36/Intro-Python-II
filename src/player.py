# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.holster = []

    def __str__(self):
        return '\nName:{self.name}\nLocation:{self.current_room}\n'.format(self=self)

    def player_move(self, direction):
        connected_room = self.current_room.new_rooms(direction)
        if connected_room is not None:
            self.current_room = connected_room

        else:
            print(f"\nTry Again")

    # def collectItem(self, item_name):


