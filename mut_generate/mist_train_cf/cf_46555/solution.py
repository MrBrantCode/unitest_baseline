"""
QUESTION:
Write a function `find_last_two_odd(input_list)` that takes a list containing both integers and strings as input. Filter out the strings and find the last two odd integers in the list. If the list contains only one odd integer, return it twice. If the list contains no odd integers, return [0, 0]. The function should return a list of the last two odd integers.
"""

def find_last_two_odd(input_list):
    # Filter the numbers and only take odd numbers
    odd_numbers = [i for i in input_list if isinstance(i, int) and i%2 != 0]
    
    # Check if the length of odd_numbers list is 1 then return the last element twice
    if len(odd_numbers) == 1:
        return [odd_numbers[-1], odd_numbers[-1]]
    # if there are no elements in the list, return [0, 0]
    elif not odd_numbers:
        return [0, 0]
    # if there are more than one elements, return the last two elements
    else:
        return odd_numbers[-2:]