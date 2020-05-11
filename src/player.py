# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.hp = 100
        self.current_room = current_room
        self.direction = None
        self.game_over = False

    def change_room(self, location, move):
        new_direction = move + "_to"

        if hasattr(location, new_direction):
            print(location, new_direction)
            return getattr(location, new_direction)

        else:
            print("Nothing lies for you that way.")
            return location

    def __str__(self):
        return f"{self.name} is in {self.current_room}"

class Inventory(Player):
    def __init__(self, name, current_room, items=[]):
        super().__init__(name, current_room)
        self.items = items

    def view_items(self):
        for i in self.items:
            print(i)
