"""
QUESTION:
Create a function `check_string` that takes a string as input and returns a boolean indicating whether the string contains only uppercase letters and numbers, the count of numbers in the string that are divisible by 3, and the indices of these divisible numbers in ascending order. The function should have a time complexity of O(n), where n is the length of the string, and return False as soon as it encounters a character that is not an uppercase letter or a digit.
"""

def check_string(string):
    divisible_count = 0
    divisible_indices = []
    
    for i, char in enumerate(string):
        if char.isupper() or char.isdigit():
            if char.isdigit() and int(char) % 3 == 0:
                divisible_count += 1
                divisible_indices.append(i)
        else:
            return False
    
    return True, divisible_count, sorted(divisible_indices)