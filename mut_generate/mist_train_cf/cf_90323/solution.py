"""
QUESTION:
Develop a function called `is_palindrome_number` that checks whether a given number is a palindrome without converting it to a string or any other data type, using a constant amount of additional space, and with a time complexity of O(log n), where n is the number of digits in the input number. The function should handle negative numbers by considering their absolute values, should not use recursion, built-in functions, or libraries for mathematical operations, and should correctly handle numbers with leading zeros and floating-point digits.
"""

def entrance(x):
    if x < 0:
        x = -x
    
    # Determine the number of digits in the input number
    n = 1
    while x >= 10**n:
        n += 1

    # Check if the number is a palindrome
    while n > 1:
        # Get the leftmost and rightmost digits
        leftmost = x // (10**(n-1))
        rightmost = x % 10

        # If the leftmost and rightmost digits are not the same, return False
        if leftmost != rightmost:
            return False

        # Remove the leftmost and rightmost digits from the number
        x = (x % (10**(n-1))) // 10

        # Update the number of digits
        n -= 2

    return True