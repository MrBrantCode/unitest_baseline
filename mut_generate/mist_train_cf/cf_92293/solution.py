"""
QUESTION:
Create a function `create_new_array` that takes an input array and returns a new array with the following conditions: 
- all elements are smaller than 5
- all elements are odd numbers
- the length of the new array does not exceed 5. 
If no elements meet the conditions, return an empty array.
"""

def create_new_array(input_array):
    """
    Creates a new array from the input array with elements that are smaller than 5, odd numbers, 
    and the length of the new array does not exceed 5.

    Args:
        input_array (list): The input list of numbers.

    Returns:
        list: A new list of numbers that meet the conditions.
    """
    new_array = []
    count = 0
    
    for num in input_array:
        if num < 5 and num % 2 != 0 and count < 5:
            new_array.append(num)
            count += 1
    
    return new_array