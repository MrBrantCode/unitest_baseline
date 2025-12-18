"""
QUESTION:
Implement the function `navigate_rooms(rooms, actions)` that takes in two parameters: 
- `rooms`: a list of dictionaries, where each dictionary represents a room with the keys: "name", "description", "actions", "next_room", and "reward".
- `actions`: a list of strings representing the sequence of actions the player will take to navigate through the rooms.

The function should return the reward obtained after completing the final room based on the provided actions. If the player attempts an invalid action or tries to navigate to a non-existent room, the function should return "Invalid action" or "Invalid room" respectively.
"""

def navigate_rooms(rooms, actions):
    current_room = 0
    for action in actions:
        if action in rooms[current_room]["actions"]:
            current_room = rooms[current_room]["next_room"]
            if current_room is None:
                return rooms[current_room - 1]["reward"]
        else:
            return "Invalid action"
    return "Invalid room"