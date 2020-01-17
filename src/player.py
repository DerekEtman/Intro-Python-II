# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
 

class Player():
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        # self.description = description

        def __str__(self):
            return f"{self.name} is in {self.current_room}"

    def travel(self, direction):
        # print(f"travel direction{direction}")

        next_room = self.current_room.get_room_in_direction(direction)

        #If we have a valid  room, move in that direction, Or else give an error message.
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cant go in that direction")
