"""
QUESTION:
Write a function called `find_recurring_integers` that takes a list of integers as input and returns a dictionary where the keys are the recurring integers and the values are their corresponding counts. The function should only include integers that appear more than once in the list.
"""

def find_recurring_integers(my_list):
    """
    Returns a dictionary of recurring integers in the input list and their counts.

    Args:
        my_list (list): A list of integers.

    Returns:
        dict: A dictionary where keys are the recurring integers and values are their counts.
    """
    # use a dictionary to keep track of the count of each integer in the list
    counter_dict = {i: my_list.count(i) for i in my_list}

    # filter out the integers that do not have recurring occurrences in the list
    recurring_integers = {k: v for k, v in counter_dict.items() if v > 1}

    return recurring_integers