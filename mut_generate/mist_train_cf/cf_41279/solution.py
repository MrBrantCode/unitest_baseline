"""
QUESTION:
Implement a function named `explore_game` that takes a list of dictionaries representing rooms in a text-based adventure game. Each dictionary should contain the keys "name", "description", "exits", "obstacle", and "outcome". The function should start the game in the first room and prompt the player to make decisions based on available exits. If the player encounters an obstacle, they should be prompted to overcome it before proceeding. The game should continue until the player reaches a room with a specific outcome, at which point the game should end and the outcome should be returned.
"""

def explore_game(rooms):
    current_room = rooms[0]
    while True:
        print(current_room["description"])
        if current_room["outcome"]:
            return current_room["outcome"]
        print("Exits:", ", ".join(current_room["exits"].keys()))
        direction = input("Choose a direction: ").lower()
        if direction in current_room["exits"]:
            next_room_name = current_room["exits"][direction]
            for room in rooms:
                if room["name"] == next_room_name:
                    next_room = room
                    break
            current_room = next_room
        else:
            print("You can't go that way. Choose a different direction.")

        if current_room["obstacle"]:
            print("You encounter an obstacle:", current_room["obstacle"])
            # Code to handle obstacle and update current_room as needed