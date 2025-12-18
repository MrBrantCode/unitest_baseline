"""
QUESTION:
Write a function called 'last_odd_numbers' that slices a given array to get the last two odd numbers. The array may contain both odd and even numbers, and the function should return the last two odd numbers in the array.
"""

def last_odd_numbers(array):
    # Use list comprehension to filter out the odd numbers
    odd_numbers = [num for num in array if num % 2 != 0]
    
    # Return the last two odd numbers using list slicing
    return odd_numbers[-2:] 