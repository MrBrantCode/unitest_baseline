"""
QUESTION:
Write a function `hexagon_sum` that calculates the total number of regular hexagons in triangular lattices for side lengths from 3 to `n`. 

The function `hexagon_sum` takes an integer `n` as input and returns the total count of all regular hexagons that can be identified by connecting any 6 lattice points in the triangular lattices. 

Restriction: `n` is an integer and `n` >= 3.
"""

def hexagon_sum(n):
    hexagon = [0]*(n+1)
    for i in range(1, (n+1)//2+1):
        j = n+2-2*i
        hexagon[j] += 3*i*j
        if j+1 <= n:
            hexagon[j+1] += 3*i*i
    return sum(hexagon[3:])  # sum the count of hexagons for side lengths from 3 to n