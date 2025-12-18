"""
QUESTION:
# Story

Those pesky rats have returned and this time they have taken over the Town Square.

The Pied Piper has been enlisted again to play his magical tune and coax all the rats towards him.

But some of the rats are deaf and are going the wrong way!

# Kata Task

How many deaf rats are there?

## Input Notes

* The Town Square is a rectangle of square paving stones (the Square has 1-15 pavers per side)
* The Pied Piper is always present

## Output Notes
* Deaf rats are those that are moving to paving stone **further away** from the Piper than where they are now
* Use Euclidian distance for your calculations

## Legend

* `P` = The Pied Piper
* `←` `↑` `→` `↓` `↖` `↗` `↘` `↙` = Rats going in different directions
* space = Everything else



# Examples

ex1 - has 1 deaf rat


↗ P              
  ↘   ↖
  ↑              
↗        


---

ex2 - has 7 deaf rats


    ↗            
P ↓   ↖ ↑
    ←   ↓
  ↖ ↙   ↙
↓ ↓ ↓
"""

from math import hypot

DIRS = {
    '←': (0, -1), '↑': (-1, 0), '→': (0, 1), '↓': (1, 0),
    '↖': (-1, -1), '↗': (-1, 1), '↘': (1, 1), '↙': (1, -1)
}

def count_deaf_rats(town):
    # Find the position of the Pied Piper
    pipper = next(((x, y) for (x, r) in enumerate(town) for (y, c) in enumerate(r) if c == 'P'))
    
    # Count the number of deaf rats
    deaf_rats_count = sum(
        is_deaf(pipper, x, y, *DIRS[c])
        for (x, r) in enumerate(town)
        for (y, c) in enumerate(r)
        if c in DIRS
    )
    
    return deaf_rats_count

def is_deaf(pipper, x, y, dx, dy):
    # Calculate the current and next distances from the Piper
    d_current, d_next = (
        hypot(*(a - b for (a, b) in zip(pipper, pos)))
        for pos in ((x, y), (x + dx, y + dy))
    )
    # Return True if the rat is deaf (moving further away)
    return d_current < d_next