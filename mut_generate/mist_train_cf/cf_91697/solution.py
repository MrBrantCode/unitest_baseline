"""
QUESTION:
Create a function called `get_odd_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list. The function should not use any built-in functions or libraries. The input list will contain a mix of even and odd integers.
"""

def get_odd_numbers(lst):
    # Initialize an empty list to store the odd numbers
    output = []
    
    # Iterate through each element in the list
    for num in lst:
        # Check if the number is odd
        if num % 2 != 0:
            # Add the odd number to the output list
            output.append(num)
            
    # Return the output list with only odd numbers
    return output