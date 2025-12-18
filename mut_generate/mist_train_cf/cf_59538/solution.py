"""
QUESTION:
Create a function `count_occurrences` that takes a list as input and returns a dictionary where keys are the unique elements from the list and their values are lists of indices where these elements are found. Avoid using built-in functions or libraries and minimize time or space complexity.
"""

def count_occurrences(lst):
    output = {}
    for i, val in enumerate(lst):
        if val not in output:
            output[val] = []
        output[val].append(i)
    return output