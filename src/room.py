# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.e_to = None
        self.w_to = None
        self.s_to = None
        self.d_to = None

    def new_rooms(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        elif direction == 'd':
            return self.d_to
        else:
            return None

    def addItem(self, item):
        self.items.append(item)

    def getItem(self, item_name):
        for i, item in enumerate(self.items):
            if item_name == item.name:
                return self.items.pop(i)

    def __str__(self):
        return_str = [
            f'Room: {self.name}',
            f'Description: {self.description}',
            f'Contents: {list(map(lambda x: x.name, self.items))}',
            ''
        ]

        return '\n\n'.join(return_str)