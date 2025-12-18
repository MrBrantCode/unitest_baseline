"""
QUESTION:
Create a function `create_dict(input_list)` that constructs a dictionary using dictionary comprehension, where the dictionary's keys are the unique elements from the input list and the values are the index of the last occurrence of each element in the list multiplied by 5. The function should handle scenarios where the input list may contain duplicate entries, in which case the value for each key will be updated with the latest pair.
"""

def create_dict(input_list):
    return {input_list[i]: i*5 for i in range(len(input_list))}