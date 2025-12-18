"""
QUESTION:
**This Kata is intended as a small challenge for my students**

All Star Code Challenge #18

Create a function called that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

Notes:
* The first argument can be an empty string  
* The second string argument will always be of length 1
"""

def count_occurrences(strng: str, letter: str) -> int:
    counter = 0
    for chr in strng:
        if chr == letter:
            counter += 1
    return counter