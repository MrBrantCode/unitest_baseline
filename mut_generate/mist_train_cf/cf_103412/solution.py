"""
QUESTION:
Create a function called `create_dictionary` that takes a list as input and returns a dictionary where the keys are the elements from the input list and the values are lists of integers. The length of each value list should be equal to the 1-based index of its corresponding key in the input list.
"""

def create_dictionary(lst):
    dictionary = {}
    for i in range(len(lst)):
        dictionary[lst[i]] = [j for j in range(i+1)]
    return dictionary