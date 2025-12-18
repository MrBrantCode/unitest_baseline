"""
QUESTION:
Create a function called `get_highest_frequency_value` that takes a dictionary, a list of integers, and an integer as parameters. The function should return the value of the dictionary corresponding to the given integer if the integer is present in the list and has the highest frequency among all the integers in the list. If the integer is not present in the list or does not have the highest frequency, the function should return None.
"""

def get_highest_frequency_value(dictionary, integer, lst):
    frequency = lst.count(integer)
    if frequency == 0:
        return None
    max_frequency = max(lst.count(num) for num in lst)
    if frequency == max_frequency:
        return dictionary.get(integer)
    else:
        return None