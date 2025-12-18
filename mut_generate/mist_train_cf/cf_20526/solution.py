"""
QUESTION:
Write a function `get_even_primes_from_sublists` that takes a list of sublists as input and returns a list of even numbers from the sublists where the sum of the sublist is a prime number. The prime number check should only consider numbers up to the square root of the sum of the sublist.
"""

def get_even_primes_from_sublists(my_list):
    """
    This function takes a list of sublists as input and returns a list of even numbers 
    from the sublists where the sum of the sublist is a prime number.

    Args:
        my_list (list): A list of sublists.

    Returns:
        list: A list of even numbers from the sublists where the sum of the sublist is a prime number.
    """
    return [x for sublist in my_list 
            if sum(sublist) > 1 and all(sum(sublist) % i != 0 for i in range(2, int(sum(sublist) ** 0.5) + 1)) 
            for x in sublist if x % 2 == 0]