"""
QUESTION:
Write a function `odd_elements` that takes a list as input and returns a new list containing only the unique elements from the input list that occur an odd number of times. The function should return unique elements.
"""

def odd_elements(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return [i for i in count_dict if count_dict[i] % 2 != 0]