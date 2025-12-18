"""
QUESTION:
Write a function named `count_divisible_by_3_and_5` to count the numbers in the range from 1 to a given upper limit (inclusive) that are divisible by both 3 and 5. The function should print the count after each iteration and return the final count.
"""

def count_divisible_by_3_and_5(upper_limit):
    """
    Counts the numbers in the range from 1 to a given upper limit (inclusive) 
    that are divisible by both 3 and 5.

    Args:
        upper_limit (int): The upper limit of the range.

    Returns:
        int: The count of numbers divisible by both 3 and 5.
    """
    counter = 0
    for number in range(1, upper_limit + 1):
        if number % 3 == 0 and number % 5 == 0:
            counter += 1
        print("Counter:", counter)
    return counter