"""
QUESTION:
# Kata Task

A bird flying high above a mountain range is able to estimate the height of the highest peak.

Can you?

# Example

## The birds-eye view



^^^^^^
 ^^^^^^^^
  ^^^^^^^
  ^^^^^
  ^^^^^^^^^^^
  ^^^^^^
  ^^^^


## The bird-brain calculations


111111
 1^^^^111
  1^^^^11
  1^^^1
  1^^^^111111
  1^^^11
  1111



111111
 12222111
  12^^211
  12^21
  12^^2111111
  122211
  1111



111111
 12222111
  1233211
  12321
  12332111111
  122211
  1111



`Height = 3`

# Series

* Bird Mountain
* [Bird Mountain - the river](https://www.codewars.com/kata/bird-mountain-the-river)
"""

def calculate_peak_height(mountain):
    M = {(r, c) for (r, l) in enumerate(mountain) for c in range(len(l)) if l[c] == '^'}
    h = 0
    while M:
        M -= {(r, c) for (r, c) in M if {(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)} - M}
        h += 1
    return h