"""
QUESTION:
Implement a function called `count_elements` that takes a list of integers as input and returns a dictionary where the keys are the integers and the values are their respective frequencies. The function should achieve this in O(n) time complexity and O(n) space complexity.
"""

def count_elements(lst):
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict