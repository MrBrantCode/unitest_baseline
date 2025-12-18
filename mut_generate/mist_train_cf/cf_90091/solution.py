"""
QUESTION:
Create a function `create_dict` that takes a list of integers as input and returns a dictionary with the even numbers from the list as keys and their squares as values. The function should have a time complexity of O(n^2), where n is the length of the list, and should not include any duplicate keys.
"""

def create_dict(lst):
    dict = {}
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if lst[i] in dict:
                dict[lst[i]] = dict[lst[i]] ** 2
            else:
                dict[lst[i]] = lst[i] ** 2
    return dict