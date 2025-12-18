"""
QUESTION:
Two strings ```a``` and b are called isomorphic if there is a one to one mapping possible for every character of ```a``` to every character of ```b```. And all occurrences of every character in ```a``` map to same character in ```b```.

## Task

In this kata you will create a function that return ```True``` if two given strings are isomorphic to each other, and ```False``` otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.

## Example
True:
```
CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS
```

False:
```
AB CC
XXY XYY
ABAB CD
```
"""

def are_isomorphic(a: str, b: str) -> bool:
    """
    Determines if two strings are isomorphic.

    Two strings are isomorphic if there is a one-to-one mapping possible for every character
    of the first string to every character of the second string, and all occurrences of every
    character in the first string map to the same character in the second string.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        bool: True if the strings are isomorphic, False otherwise.
    """
    return [a.index(x) for x in a] == [b.index(y) for y in b]