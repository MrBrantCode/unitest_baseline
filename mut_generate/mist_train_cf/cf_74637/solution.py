"""
QUESTION:
Write a function called `non_unique_elements` that takes a list of elements as input and returns a tuple containing three values: 
1. A list of non-unique elements from the input list, 
2. The sum of the occurrences of all elements in the input list, and 
3. A dictionary where the keys are the non-unique elements and the values are lists of their corresponding indices in the input list.
"""

from collections import Counter

def non_unique_elements(lst):
    count = Counter(lst)
    non_unique = [item for item in lst if count[item] > 1]
    erroneous_elements = {item: [i for i in range(len(lst)) if lst[i] == item] for item in non_unique}
    return non_unique, sum(count.values()), erroneous_elements