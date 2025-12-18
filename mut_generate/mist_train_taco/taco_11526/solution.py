"""
QUESTION:
*This kata is based on [Project Euler Problem #349](https://projecteuler.net/problem=349). You may want to start with solving [this kata](https://www.codewars.com/kata/langtons-ant) first.*

---

[Langton's ant](https://en.wikipedia.org/wiki/Langton%27s_ant) moves on a regular grid of squares that are coloured either black or white.
The ant is always oriented in one of the cardinal directions (left, right, up or down) and moves  according to the following rules:
- if it is on a black square, it flips the colour of the square to white, rotates 90 degrees counterclockwise and moves forward one square.
- if it is on a white square, it flips the colour of the square to black, rotates 90 degrees clockwise and moves forward one square.

Starting with a grid that is **entirely white**, how many squares are black after `n` moves of the ant?

**Note:** `n` will go as high as 10^(20)

---

## My other katas

If you enjoyed this kata then please try [my other katas](https://www.codewars.com/collections/katas-created-by-anter69)! :-)

#### *Translations are welcome!*
"""

def count_black_squares_after_moves(n):
    move = [lambda p: (p[0] + 1, p[1]), lambda p: (p[0], p[1] + 1), lambda p: (p[0] - 1, p[1]), lambda p: (p[0], p[1] - 1)]
    (start, loop, size) = (9977, 104, 12)
    
    (pos, d, black, res) = ((0, 0), 0, set(), 0)
    
    if n > start:
        x = (n - start) % loop
        res = size * (n - start - x) // loop
        n = start + x
    
    for i in range(n):
        if pos in black:
            black.remove(pos)
            d = (d + 1) % 4
        else:
            black.add(pos)
            d = (d - 1) % 4
        pos = move[d](pos)
    
    return res + len(black)