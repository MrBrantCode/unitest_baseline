"""
QUESTION:
# Kata Task

Given a list of random integers, return the Three Amigos.

These are 3 numbers that live next to each other in the list, and who have the **most** in common with each other by these rules:
* lowest statistical range
* same parity

# Notes

* The list will contain at least 3 numbers
* If there is more than one answer then return the first one found (reading the list left to right)
* If there is no answer (e.g. no 3 adjacent numbers with same parity) then return an empty list.

# Examples

* ex1
 * Input = ```[1, 2, 34, 2, 1, 5, 3, 5, 7, 234, 2, 1]```
 * Result = ```[5,3,5]```
 

* ex2
 * Input = ```[2, 4, 6, 8, 10, 2, 2, 2, 1, 1, 1, 5, 3]```
 * Result = ```[2,2,2]```
 

* ex3
 * Input = ```[2, 4, 5, 3, 6, 3, 1, 56, 7, 6, 3, 12]```
 * Result = ```[]```
"""

def find_three_amigos(numbers):
    """
    Finds the Three Amigos in a list of integers.

    The Three Amigos are three adjacent numbers in the list that:
    1. Have the same parity (all even or all odd).
    2. Have the lowest statistical range (difference between the maximum and minimum values).

    If multiple triplets meet the criteria, the first one found (reading left to right) is returned.
    If no such triplet exists, an empty list is returned.

    Parameters:
    - numbers (list of int): The list of integers to search.

    Returns:
    - list of int: A list containing the three adjacent numbers that meet the criteria, or an empty list if no such triplet exists.
    """
    return min(([a, b, c] for (a, b, c) in zip(numbers, numbers[1:], numbers[2:]) if a % 2 == b % 2 == c % 2), key=lambda triple: max(triple) - min(triple), default=[])