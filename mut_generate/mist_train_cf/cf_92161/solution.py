"""
QUESTION:
Create a function named `find_intersection` that takes two lists of integers as input and returns a list containing the common elements. The function should handle duplicate elements in the input lists by including each common element a number of times equal to the minimum of its counts in the two input lists. The function should not modify the input lists.
"""

from collections import Counter

def find_intersection(list1, list2):
    intersection = []
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    for num, count in counter1.items():
        if count > 0 and counter2[num] > 0:
            intersection.extend([num] * min(count, counter2[num]))
    
    return intersection