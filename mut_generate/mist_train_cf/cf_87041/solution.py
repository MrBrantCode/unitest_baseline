"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers as input, removes any negative numbers and numbers divisible by 3, and returns a new list containing the remaining unique elements in their original order.
"""

def remove_duplicates(numbers):
    # Create a new list to store the unique elements
    unique_numbers = []
    
    # Iterate over the input list
    for num in numbers:
        # Ignore negative numbers and numbers divisible by 3
        if num >= 0 and num % 3 != 0:
            # Add the number to the unique list if it's not already present
            if num not in unique_numbers:
                unique_numbers.append(num)
    
    return unique_numbers