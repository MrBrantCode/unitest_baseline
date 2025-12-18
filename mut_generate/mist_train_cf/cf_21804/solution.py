"""
QUESTION:
Write a function `check_strings` that takes an array of strings as input and returns a boolean. The function should return True if all strings in the array contain at least two digits and two uppercase letters, and False otherwise.
"""

def check_strings(arr):
    count = 0
    for string in arr:
        digits = 0
        uppercase = 0
        for char in string:
            if char.isdigit():
                digits += 1
            elif char.isupper():
                uppercase += 1
            if digits >= 2 and uppercase >= 2:
                count += 1
                break
    return count == len(arr)