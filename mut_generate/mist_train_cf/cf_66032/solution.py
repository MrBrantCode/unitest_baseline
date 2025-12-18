"""
QUESTION:
Develop a function `correct_program(str1, str2)` that checks if all digits of the second number string (`str2`) are in the same order in the first number string (`str1`). The function should preserve the order and occurrence of digits in `str1` and `str2`. The function should return `True` if all digits of `str2` are in the same order in `str1`, and `False` otherwise.
"""

def correct_program(str1, str2):
    index = 0
    for i in str2:
        found_at = str1.find(i, index)
        if found_at == -1:
            return False
        else:
            # Start the next search from the found index + 1
            index = found_at + 1
            
    return True