"""
QUESTION:
Write a Python function named `verify_number` that takes an integer value as input, checks if it is a three-digit number, and satisfies three conditions:

- The digit in the hundredths place is twice the digit in the ones place.
- The digit in the tens place is 3 more than the digit in the ones place.
- If the digit in the ones place and the digit in the hundreds place were swapped, the new number would decrease by 297.

Restrictions: The input is a three-digit integer.
"""

def verify_number(n):
    n_str = str(n)
    
    # Check if the number is a three-digit number
    if len(n_str) != 3:
        return False
    
    ones = int(n_str[2])
    tens = int(n_str[1])
    hundreds = int(n_str[0])
    
    # Check if the digit in the hundreds place is twice the digit in the ones place
    if hundreds != 2 * ones:
        return False
    
    # Check if the digit in the tens place is 3 more than the digit in the ones place
    if tens != ones + 3:
        return False

    # Check if the number created after swapping the digits in the hundreds and ones places is less by 297
    swapped_n = (ones * 100) + (tens * 10) + hundreds
    if (n - swapped_n) != 297:
        return False
    
    return True