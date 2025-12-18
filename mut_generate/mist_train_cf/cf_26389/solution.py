"""
QUESTION:
Implement a function `find_connected_rooms(rooms, start_room)` that takes in a graph represented as an adjacency list `rooms` and the identifier of a starting room `start_room`. The function should use depth-first search (DFS) to traverse the graph and return a list of all the rooms that are connected to the starting room, including the starting room itself.

Restrictions:
- Use a stack to keep track of the rooms to visit.
- Use a dictionary to keep track of the rooms that have been visited, initialized with all rooms set to `False`.
- The function should continue the DFS until the stack is empty.
"""

def find_connected_rooms(rooms: dict, start_room: int) -> list:
    stack = [start_room]
    seen = {room: False for room in rooms}
    connected_rooms = []

    while stack:
        room_idx = stack.pop()
        if not seen[room_idx]:
            seen[room_idx] = True
            connected_rooms.append(room_idx)
            for key in rooms[room_idx]:
                if not seen[key]:
                    stack.append(key)

    return connected_rooms