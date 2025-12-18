"""
QUESTION:
Write a function named `find_longest_fruit` that accepts a list of fruit names in string format. The function should return the fruit name with the maximum character length. In the event of a tie, return the fruit that appears first in alphabetical order. The function must also handle the case where the input list is empty.
"""

def find_longest_fruit(fruits):
    if not fruits:
        return None
    # If lengths are equal, sorted by name. Else, sorted by length, descending.
    fruits = sorted(fruits, key=lambda x: (-len(x), x)) 
    return fruits[0]