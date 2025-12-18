"""
QUESTION:
Create a function named `create_dict` that takes a list of integers as input and returns a dictionary. The function should have a time complexity of O(n^2). The dictionary should only include the elements from the list that are divisible by 2, with no duplicate keys, and the corresponding values should be the square of the keys.
"""

def create_dict(lst):
    result = {}
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] not in result.keys():
            result[lst[i]] = lst[i]**2
    return result