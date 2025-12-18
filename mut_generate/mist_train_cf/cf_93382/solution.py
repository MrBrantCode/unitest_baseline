"""
QUESTION:
Design a function named `is_number_equal_to_reverse` that takes an integer as input and returns a boolean value indicating whether the number is equal to its reverse. The function should be efficient in terms of both time and space complexity, handling numbers with up to 10^6 digits.
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