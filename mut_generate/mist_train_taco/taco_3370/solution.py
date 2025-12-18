"""
QUESTION:
You will be given a string. 

You need to return an array of three strings by gradually pulling apart the string.

You should repeat the following steps until the string length is 1:

a) remove the final character from the original string, add to solution string 1.
b) remove the first character from the original string, add to solution string 2.

The final solution string value is made up of the remaining character from the original string, once originalstring.length == 1.

Example:

"exampletesthere"
becomes:
["erehtse","example","t"]

The Kata title gives a hint of one technique to solve.
"""

def split_string_by_pop_shift(s: str) -> list[str]:
    l1 = list(s)
    l2 = []
    l3 = []
    while len(l1) > 1:
        l2.append(l1.pop())
        l3.append(l1.pop(0))
    return [''.join(l2), ''.join(l3), ''.join(l1)]