"""
QUESTION:
Write a function named `find_max` that takes a list of numbers as input and returns a tuple containing the maximum value in the list and a list of indices where this maximum value occurs. The function should not use Python's built-in `max()` or `index()` functions. If there are multiple instances of the same highest value, the function should return all their index locations.
"""

def find_max(lst):
    max_num = lst[0]
    max_index = [0]  # Consider first value as a potential max value
    for i in range(1, len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            max_index = [i]    # If the new number is greater, update max_num and reinitialize max_index
        elif lst[i] == max_num:
            max_index.append(i)   # If the number is equal to max_num, just append its index to max_index
    return max_num, max_index