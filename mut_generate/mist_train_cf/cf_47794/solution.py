"""
QUESTION:
Implement a function `highest_palindrome(low, high)` that returns the highest palindrome number within the given integer range `[low, high]`, or 0 if no palindrome is found. The function should be able to handle large ranges efficiently, with a time complexity of O(n*k), where n is the difference between high and low, and k is the number of digits in the integer.
"""

def highest_palindrome(low, high):
    """Function to return the highest palindrome integer within the given range, 
    or zero if no palindrome found"""
    # reversed list to start with the highest number in the range
    for i in range(high, low - 1, -1):
        # check if the number is same when its digits are reversed
        if str(i) == str(i)[::-1]:
            return i
    return 0