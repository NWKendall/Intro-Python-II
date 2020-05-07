# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.hp = 100
        self.current_room = current_room
        self.direction = None
        self.game_over = False
    
    # need move function here
    def explore(self):
        print(f"**{self.name} moved to {self.current_room}**")

    def __str__(self):
        return f"{self.name} is in {self.current_room}"


