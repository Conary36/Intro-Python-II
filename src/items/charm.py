from src.items.item import Item


class Charm(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

    def __str__(self):
        return f"\n{self.name}\n{self.description}\n with a power of {self.defense}"
