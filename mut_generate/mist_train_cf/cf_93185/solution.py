"""
QUESTION:
Create a function `get_multiple_of_three` that takes a string of up to 100 characters as input. The function should filter out non-digit characters, sort the remaining digits in ascending order, and return the smallest possible 5-digit number that is a multiple of 3. If no such number can be formed, return None.
"""

def get_multiple_of_three(input_string):
    # Initialize a list to store the numerical characters
    numbers = []
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a numerical digit
        if char.isdigit():
            # Add the digit to the list
            numbers.append(int(char))
    
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Find the smallest multiple of 3 with exactly 5 digits
    for i in range(10000, 100000):
        if i % 3 == 0:
            return i
    
    # If no multiple of 3 with exactly 5 digits is found, return None
    return None