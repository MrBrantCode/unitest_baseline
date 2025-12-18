"""
QUESTION:
Implement a function `get_color_tint(block_id, y, block_ignore)` that takes in a block ID (string), a y-coordinate (integer), and a list of block IDs to ignore (list of strings). The function should return the color tint in HSL format (a dictionary containing 'h', 's', and 'l' values) based on the following rules:

- If the block ID is 'grass', return {'h':93, 's':39, 'l':10} if y > 0 and {'h':114, 's':64, 'l':22} if y <= 0.
- If the block ID is 'ice', return {'h':240, 's':5, 'l':95}.
- If the block ID is 'fire', return {'h':55, 's':100, 'l':50}.
- If the block ID is in the block_ignore list or y is 0, store the ground height and return it instead of the color tint.

Note: The function should return a dictionary containing 'h', 's', and 'l' values if a color tint is determined, or a dictionary containing the ground height if no color tint is determined.
"""

def get_color_tint(block_id, y, block_ignore):
    if block_id in block_ignore or y == 0:
        return {'ground_height': y}

    if block_id == 'grass':
        return {'h': 93, 's': 39, 'l': 10} if y > 0 else {'h': 114, 's': 64, 'l': 22}
    elif block_id == 'ice':
        return {'h': 240, 's': 5, 'l': 95}
    elif block_id == 'fire':
        return {'h': 55, 's': 100, 'l': 50}