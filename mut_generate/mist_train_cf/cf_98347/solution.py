"""
QUESTION:
Write a function `find_coordinates` that takes a list of strings and target coordinates as input, where each string represents a sequence of directions ('N', 'S', 'E', 'W'), and returns a list of all coordinates that match the target.
"""

def find_coordinates(strings, target_x, target_y):
    matches = []
    for string in strings:
        x, y = 0, 0
        for direction in string:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
        if x == target_x and y == target_y:
            matches.append((x, y))
    return matches