"""
QUESTION:
Create a function `extract_elements(lst)` that takes a list of integers as input and returns a list containing the second, third, fourth elements, and the last two elements in reverse order. The input list size ranges from 5 to 1,000,000 entries. Do not use built-in slicing methods.
"""

def extract_elements(lst):
    if len(lst) < 5:
        return "List should have at least 5 elements"
    second = lst[1]
    third = lst[2]
    fourth = lst[3]
    last_two = [lst[-2], lst[-1]]
    return [second, third, fourth] + last_two[::-1]