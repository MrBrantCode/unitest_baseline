"""
QUESTION:
The cat wants to lay down on the table, but the problem is that we don't know where it is in the room!

You'll get in input:
 - the cat coordinates as a list of length 2, with the row on the map and the column on the map.
 - the map of the room as a list of lists where every element can be 0 if empty or 1 if is the table (there can be only one 1 in the room / lists will never be empty).

# Task:

You'll need to return the route to the table, beginning from the cat's starting coordinates, as a String. The route must be a sequence of letters U, D, R, L that means Up, Down, Right, Left. The order of the letters in the output isn't important.

# Outputs:

* The route for the cat to reach the table, as a string
* If there isn't a table in the room you must return "NoTable"
* if the cat is outside of the room you must return "NoCat" (this output has the precedence on the above one).
* If the cat is alredy on the table, you can return an empty String.

# Example: 

```
cat = [0,1]
room =[[0,0,0], [0,0,0], [0,0,1]]

The route will be "RDD", or "DRD" or "DDR"
```
"""

def find_cat_route_to_table(cat, room):
    # Unpack cat coordinates
    cy, cx = cat
    # Get room dimensions
    h, w = len(room), len(room[0])
    
    # Check if cat is outside the room
    if not (0 <= cy < h and 0 <= cx < w):
        return 'NoCat'
    
    # Find the table coordinates
    table_coords = next(((y, x) for y in range(h) for x in range(w) if room[y][x] == 1), (-1, -1))
    ty, tx = table_coords
    
    # Check if there is no table in the room
    if ty == -1:
        return 'NoTable'
    
    # Determine vertical and horizontal movements
    ver = 'U' if ty < cy else 'D'
    dy = abs(ty - cy)
    
    hor = 'L' if tx < cx else 'R'
    dx = abs(tx - cx)
    
    # Construct the route string
    route = f'{hor * dx}{ver * dy}'
    
    return route