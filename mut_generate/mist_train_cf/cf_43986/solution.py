"""
QUESTION:
Write a function `count_elements` that takes an array as input and returns a dictionary where the keys are the unique elements from the array and the values are their corresponding counts.
"""

def count_elements(arr):
    count_dict = {}
    for elem in arr:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    return count_dict