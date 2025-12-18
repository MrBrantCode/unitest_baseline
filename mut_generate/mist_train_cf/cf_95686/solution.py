"""
QUESTION:
Write a function `check_string` that takes a string as input. The function should return a tuple containing a boolean value and a count. The boolean value should be `True` if the string consists only of uppercase letters and digits that are divisible by 3, and `False` otherwise. The count should be the number of digits in the string that are divisible by 3. The function should have a time complexity of O(n), where n is the length of the string.
"""

def check_string(input_string):
    count = 0
    for char in input_string:
        if char.isupper():
            continue
        elif char.isdigit():
            num = int(char)
            if num % 3 == 0:
                count += 1
            else:
                return False, 0
        else:
            return False, 0
    return True, count