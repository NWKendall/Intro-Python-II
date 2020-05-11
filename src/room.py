# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, room_name, description):
        self.room_name = room_name
        self.description = description
        self.visited = False
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        return f"{self.room_name}. {self.description}"

class List(Room):
    def __init__(self, room_name, description, loot=[]):
        super().__init__(room_name, description)
        self.loot = loot
    
    def search(self):
        for l in self.loot:
            print(l)
