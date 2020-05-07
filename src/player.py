# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.hp = 100
        self.current_room = current_room
        self.direction = None
        self.game_over = False
    
    def change_room(self, current_room, move):
        new_location = move + "_to"

        if hasattr(current_room, new_location):
            print(current_room, new_location)
            return getattr(current_room, new_location)
            
        return current_room


    def __str__(self):
        return f"{self.name} is in {self.current_room}"
        

class Inventory(Player):
    def __init__(self, name, current_room, items=[]):
        super().__init__(name, current_room)
        self.items = items
    
    def view_items(self):
        for i in self.items:
            print(i)

