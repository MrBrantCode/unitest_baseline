"""
QUESTION:
Create a function `check_string` that takes a string as input and returns a tuple. The string should only contain uppercase letters and numbers. The function should return a boolean value indicating whether the string meets the requirements and the count of numbers in the string that are divisible by 3. The function should have a time complexity of O(n), where n is the length of the string.
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
                return False
        else:
            return False
    return count, True