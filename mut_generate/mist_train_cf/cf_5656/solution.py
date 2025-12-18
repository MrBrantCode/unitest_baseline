"""
QUESTION:
Write a function `power_of_3` that takes an integer `limit` as input and prints the powers of 3 up to the given limit. The function should validate that the limit is a positive integer not exceeding 100 and the sum of the powers of 3 does not exceed 2000. If the limit is invalid or the sum of powers exceeds 2000, print an error message.
"""

def entrance(limit):
    """
    Prints the powers of 3 up to the given limit.

    Args:
        limit (int): The upper limit for printing powers of 3.

    Returns:
        None
    """
    if limit <= 0 or limit > 100:
        print("Invalid limit")
        return
    power_sum = 0
    for i in range(limit):
        power = 3 ** i
        power_sum += power
        if power_sum > 2000:
            print("Sum of powers exceeds 2000")
            return
        print(power)