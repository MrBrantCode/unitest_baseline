"""
QUESTION:
Create a function named `create_dictionary` that takes a list of integers as input. The function should return a dictionary containing key-value pairs where the keys are the even integers from the list and the values are the sum of all the odd integers that come after each even integer. The dictionary should only include even integers that have at least one odd integer following them in the input list.
"""

def create_dictionary(lst):
    dictionary = {}
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i < len(lst) - 1:
            following_numbers = [lst[j] for j in range(i + 1, len(lst)) if lst[j] % 2 != 0]
            if following_numbers:
                dictionary[lst[i]] = sum(following_numbers)
    return dictionary