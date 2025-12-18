"""
QUESTION:
Create a function called `count_elements` that takes a list as input and returns a dictionary where the keys are the unique elements in the list and the values are the counts of their occurrences. The function should be able to handle lists with any format, including those with a mixture of numeric and string data types.
"""

def count_elements(lst):
    unique_dict = {}
    for i in lst:
        if i in unique_dict:
            unique_dict[i] += 1
        else:
            unique_dict[i] = 1
    return unique_dict