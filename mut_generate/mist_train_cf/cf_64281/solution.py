"""
QUESTION:
Write a function `ways_to_fill(length)` that calculates the number of ways to fill a row of length units with blue blocks, subject to the following restrictions:

- Each blue block has a minimum length of four units.
- Any two blue blocks are separated by at least two white squares.
- The total length of the row is given by the input parameter `length`.
- Blue blocks of different lengths can be mixed.

Return the total number of ways to fill the row of the given length.
"""

def ways_to_fill(length):
    ways = [1, 1, 1, 1] + [0] * (length - 3) 
    for i in range(4, length + 1):
        ways[i] += ways[i-1]
        ways[i] += ways[i-4]
        for j in range(0, i - 4):  
            ways[i] += ways[j]
    return ways[length]