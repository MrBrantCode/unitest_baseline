"""
QUESTION:
Implement a function `unique_elements(input_list)` that takes a list of integers as input and returns a new list containing only the unique elements from the input list, preserving their original order. The function should be able to handle a list containing any type of hashable elements, including integers, strings, and tuples. The input list can contain duplicate elements.
"""

def unique_elements(input_list):
    ans = []
    seen = set()  
    for i in input_list:
        if i not in seen:  
            ans.append(i)  
            seen.add(i)  
    return ans