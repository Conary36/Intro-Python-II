# Write a class to hold player information, e.g. what room they are in
# currently.

from src.items.item import Item


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

    def collectItem(self, Item):
        found = self.current_room.get_item(Item)

        if found:
            self.holster.append(found)
            print(f'{found}')
        else:
            print('NOPE, not here!')

    def putDownItem(self, Item):
        dumped = None
        for i, item in enumerate(self.holster):
            if Item == Item:
                dumped = self.holster.pop(i)
                break
        if dumped:
            self.holster.remove(self.Item)
            return f"{self.holster}"

        # else:
        #     print('No items to get rid of')

    def holsterItems(self,):
        print('items:')

        if not len(self.holster):
            print('(empty)')
            print()
            return
        print("\n".join(map(lambda x: f'{x.name}: {x.description}', self.holster)))
