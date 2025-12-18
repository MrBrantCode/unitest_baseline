"""
QUESTION:
Write a function called `find_unique_with_frequency` that takes two lists of strings as input. The function should identify the non-overlapping elements in the two lists and return their frequency.
"""

from collections import Counter

def find_unique_with_frequency(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    unique1 = set(list1) - set(list2)
    unique2 = set(list2) - set(list1)
    
    unique_count1 = {item: counter1[item] for item in unique1}
    unique_count2 = {item: counter2[item] for item in unique2}
    
    return unique_count1, unique_count2