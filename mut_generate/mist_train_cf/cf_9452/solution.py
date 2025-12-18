"""
QUESTION:
Design a function called `is_palindrome(num)` that checks if a given number is a palindrome. The function should have a time complexity of O(log n), where n is the number of digits in the input number. The function should return `True` if the number is a palindrome and `False` otherwise.
"""

def is_palindrome(num):
    num_str = str(num)
    start = 0
    end = len(num_str) - 1
    
    while start <= end:
        if num_str[start] != num_str[end]:
            return False
        start += 1
        end -= 1
    
    return True