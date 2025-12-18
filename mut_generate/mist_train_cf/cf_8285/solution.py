"""
QUESTION:
Create a function `is_palindrome_number` that takes an integer as input and returns `True` if the absolute value of the integer is a palindrome and `False` otherwise. The function should have a time complexity of O(log n), where n is the number of digits in the input number, and should use a constant amount of additional space. The function should not convert the input number to a string or any other data type, should not use any built-in functions or libraries for mathematical operations, and should not use recursion.
"""

def is_palindrome_number(num):
    if num < 0:
        num = -num
    
    # Determine the number of digits in the input number
    n = 1
    while num >= 10**n:
        n += 1

    # Check if the number is a palindrome
    while n > 1:
        # Get the leftmost and rightmost digits
        leftmost = num // (10**(n-1))
        rightmost = num % 10

        # If the leftmost and rightmost digits are not the same, return False
        if leftmost != rightmost:
            return False

        # Remove the leftmost and rightmost digits from the number
        num = (num % (10**(n-1))) // 10

        # Update the number of digits
        n -= 2

    return True