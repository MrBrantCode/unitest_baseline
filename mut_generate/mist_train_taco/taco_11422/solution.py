"""
QUESTION:
Several ages ago Berland was a kingdom. The King of Berland adored math. That's why, when he first visited one of his many palaces, he first of all paid attention to the floor in one hall. The floor was tiled with hexagonal tiles.

The hall also turned out hexagonal in its shape. The King walked along the perimeter of the hall and concluded that each of the six sides has a, b, c, a, b and c adjacent tiles, correspondingly.

To better visualize the situation, look at the picture showing a similar hexagon for a = 2, b = 3 and c = 4.

<image>

According to the legend, as the King of Berland obtained the values a, b and c, he almost immediately calculated the total number of tiles on the hall floor. Can you do the same?

Input

The first line contains three integers: a, b and c (2 ≤ a, b, c ≤ 1000).

Output

Print a single number — the total number of tiles on the hall floor.

Examples

Input

2 3 4


Output

18
"""

def calculate_hexagonal_tiles(a: int, b: int, c: int) -> int:
    # Sort the sides to ensure a <= b <= c
    sorted_sides = sorted([a, b, c])
    
    # Extract the sorted sides
    a_sorted, b_sorted, c_sorted = sorted_sides
    
    # Calculate the total number of tiles using the formula
    total_tiles = (b_sorted + a_sorted - 1) * (c_sorted + a_sorted - 1) - (a_sorted - 1) * a_sorted
    
    return total_tiles