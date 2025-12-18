"""
QUESTION:
Create a function called `five_highest_elements` that takes a list of integers as input and returns a list of the five highest elements. The input list may contain fewer than five elements, in which case the function should return all elements in the list. The function should return the highest elements in descending order, and should be able to handle duplicate elements.
"""

def five_highest_elements(num_list):
    num_list.sort(reverse = True)
    return num_list[:5]