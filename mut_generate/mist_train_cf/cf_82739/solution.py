"""
QUESTION:
Write a function called `find_lowest_even_highest_odd` that takes a list of integers as input and returns two lists. The first list should contain the three lowest even numbers from the input list, and the second list should contain the three highest odd numbers from the input list. You cannot use any built-in or third-party sorting functions.
"""

def find_lowest_even_highest_odd(dataset):
    even_list = []
    odd_list = []

    for num in dataset:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)

    # find 3 lowest even numbers
    even_lowest = []
    for _ in range(3):
        if even_list:  # Check if the list is not empty
            min_value = min(even_list)
            even_lowest.append(min_value)
            even_list.remove(min_value)

    # find 3 highest odd numbers
    odd_highest = []
    for _ in range(3):
        if odd_list:  # Check if the list is not empty
            max_value = max(odd_list)
            odd_highest.append(max_value)
            odd_list.remove(max_value)

    return even_lowest, odd_highest