"""
QUESTION:
Create a function named `solve_problem` that takes a list of integers as input and returns a new list with the same order. The function should replace any integer that is a multiple of 4 with its prime number successor (the next prime number greater than the given integer).
"""

def find_next_prime(num):
    def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime = num
    found = False

    while not found:
        prime += 1
        if is_prime(prime):
            found = True

    return prime


def solve_problem(lst):
    """
    This function takes a list of integers, replaces any integer that is a multiple of 4 
    with its prime number successor (the next prime number greater than the given integer), 
    and returns the new list.

    Args:
        lst (list): A list of integers.

    Returns:
        list: The new list with multiples of 4 replaced by their prime successors.
    """
    result = []
    for num in lst:
        if num % 4 == 0:
            result.append(find_next_prime(num))
        else:
            result.append(num)

    return result