"""
QUESTION:
Create a function called `is_armstrong_number` that takes a positive integer `num` as input and returns a boolean value indicating whether the number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. The function should have a time complexity of O(log n), where n is the input number.
"""

def is_armstrong_number(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Get the length of the number
    length = len(num_str)
    
    # Calculate the sum of powers of each digit
    armstrong_sum = sum(int(digit) ** length for digit in num_str)
    
    # Check if the calculated sum is equal to the given number
    return armstrong_sum == num