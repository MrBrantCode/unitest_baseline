"""
QUESTION:
Implement a function `is_palindrome(num)` that determines whether a given integer is a palindrome. The function should return True if the number is a palindrome and False otherwise. The input number can be of any size and the solution must achieve a time complexity of O(log n), where n is the number of digits in the input number.
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