# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.holster = []

    def __str__(self):
        return '\nName:{self.name}\nLocation:{self.current_room}\n'.format(self=self)

    def collectItem(self, item_name):
        y = [v ]
