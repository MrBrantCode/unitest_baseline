"""
QUESTION:
Implement the function `add_beacon` that adds a beacon pattern to the universe grid. The function takes the following parameters: 
- `universe`: A boolean grid representing the universe.
- `x`: The x-coordinate of the top-left corner of the beacon pattern.
- `y`: The y-coordinate of the top-left corner of the beacon pattern.
- `type`: An optional parameter specifying the type of beacon pattern, either '\\' or '/'.

The function should add the beacon pattern to the universe grid based on the given type, using the `add_block` function which adds a live cell to the universe grid at the specified coordinates. The beacon pattern for type '\\' consists of two blocks forming a diagonal pattern, and for type '/' it consists of two blocks forming a horizontal pattern.
"""

def add_beacon(universe, x, y, type='\\'):
    width = int(len(universe) ** 0.5)
    universe = universe.reshape((width, width))

    if type == '\\':
        universe[y, x] = True
        universe[y + 2, x + 2] = True
    elif type == '/':
        universe[y, x + 1] = True
        universe[y + 1, x + 2] = True
        universe[y + 2, x] = True
        universe[y + 3, x + 1] = True

    return universe.flatten()