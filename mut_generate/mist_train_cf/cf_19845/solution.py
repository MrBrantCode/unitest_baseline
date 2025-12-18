"""
QUESTION:
Create a function called `countDuplicates` that takes a list of integers as input and returns the number of unique duplicate elements in the list. The function should not modify the original list. 

The input list can be empty, contain negative numbers, or have duplicate elements in any order. The function should count each unique duplicate element only once.
"""

def countDuplicates(lst):
    unique = set(lst)
    count = 0
    for num in unique:
        occurrences = lst.count(num)
        if occurrences > 1:
            count += 1
    return count