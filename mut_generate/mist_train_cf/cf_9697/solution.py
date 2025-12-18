"""
QUESTION:
Write a function called `find_second_highest_odd` that takes a list of integers as input and returns the second highest odd value in the list. If there is no odd value or only one odd value in the list, return -1.
"""

def find_second_highest_odd(arr):
    # Filter out the odd numbers from the array
    odd_numbers = [num for num in arr if num % 2 != 0]
    
    # If there are less than 2 odd numbers, return -1
    if len(odd_numbers) < 2:
        return -1
    
    # Remove the highest odd number and return the highest of the remaining numbers
    odd_numbers.remove(max(odd_numbers))
    return max(odd_numbers)