"""
QUESTION:
Implement the `orderNext_getTile` function to return the next tile in a sequence based on the input integer `le_n`. If there are no more tiles, the function should return `False`. Implement the `orderNext_reTile` function to return an iterator that yields a modified sequence of tiles based on the input tile, where even tiles are doubled and odd tiles are prefixed with '-'.
"""

def orderNext_getTile(le_n):
    if le_n < 10:
        return le_n + 1
    else:
        return False  

def orderNext_reTile(tile):
    if tile % 2 == 0:
        yield tile * 2  
    else:
        yield '-' + str(tile)