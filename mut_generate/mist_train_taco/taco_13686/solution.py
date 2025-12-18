"""
QUESTION:
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters `R`, `G`, and `B`.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colours.

Examples:

```
"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9
```
"""

def min_removals_for_alternating_stones(stones: str) -> int:
    """
    Calculate the minimum number of stones that need to be removed from the table
    so that no two adjacent stones have the same color.

    Parameters:
    stones (str): A string representing the sequence of stones on the table.

    Returns:
    int: The minimum number of stones to remove.
    """
    removals = sum(1 for i in range(1, len(stones)) if stones[i - 1] == stones[i])
    return removals