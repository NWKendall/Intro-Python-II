# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room_name, current_room, direction, hp):
        self.room_name = room_name
        self.current_room = current_room
        self.direction = direction
        self.hp = hp

    def __str__(self):
        return f"{self.name} is in {self.current_room}"


