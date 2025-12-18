"""
QUESTION:
Write a function called `find_coordinates` that takes a list of strings and two integers as input, representing target x and y coordinates on a two-dimensional plane. Each string contains directions 'N' (north), 'S' (south), 'E' (east), and 'W' (west). The function should return a list of coordinates that match the target coordinates after following the directions in each string.
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