"""
QUESTION:
Create a function called `tuple_to_dict` that takes a list of tuples as input, where each tuple contains a string and an integer. The function should return a dictionary where the keys are the strings from the tuples and the values are the integers. The function should only include tuples in the resulting dictionary where the string has a maximum length of 10 characters and the integer is divisible by 3. The function must have a time complexity of O(n), where n is the length of the input list.
"""

def tuple_to_dict(list_tuples):
    result = {}
    for tuple in list_tuples:
        if len(tuple[0]) <= 10 and tuple[1] % 3 == 0:
            result[tuple[0]] = tuple[1]
    return result