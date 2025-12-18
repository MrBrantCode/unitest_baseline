"""
QUESTION:
Write a function called `remove_duplicates` that takes a list of integers as input and returns a new list. The function should maintain the original order of the remaining elements and exclude any negative numbers and numbers divisible by 3. The output list should contain unique numbers only.
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