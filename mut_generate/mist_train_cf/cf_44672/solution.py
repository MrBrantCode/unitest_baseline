"""
QUESTION:
Create a function called `count_elements` that takes a nested list and an empty dictionary as input. The function should recursively traverse the nested list and count the frequency of each element, including duplicates and elements within nested lists, and store the counts in the dictionary.
"""

def count_elements(lst, counter):
    for item in lst:
        if isinstance(item, list):
            count_elements(item, counter)
        elif item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    return counter