"""
QUESTION:
Create a function called `count_and_skip` that takes an integer `n` as input and prints each number from 1 to `n` (inclusive) that is not divisible by both 3 and 4. Additionally, return a list of numbers that are divisible by both 3 and 4.
"""

def count_and_skip(n):
    """
    Prints each number from 1 to n (inclusive) that is not divisible by both 3 and 4.
    Returns a list of numbers that are divisible by both 3 and 4.

    Args:
        n (int): The upper limit of the range.

    Returns:
        list: A list of numbers divisible by both 3 and 4.
    """
    skipped_numbers = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            skipped_numbers.append(i)
        else:
            print(i)
    return skipped_numbers