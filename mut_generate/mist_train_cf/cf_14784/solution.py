"""
QUESTION:
Write a function `is_number_equal_to_reverse(num: int)` that checks if a given integer `num` is equal to its reverse. The function should return `True` if the two numbers are equal and `False` otherwise. The input integer can have up to 10^6 digits. Minimize both time and space complexity.
"""

def is_number_equal_to_reverse(num: int) -> bool:
    num_str = str(num)
    num_len = len(num_str)
    rev_ptr = num_len - 1

    for i in range(num_len // 2):
        if num_str[i] != num_str[rev_ptr]:
            return False
        rev_ptr -= 1

    return True