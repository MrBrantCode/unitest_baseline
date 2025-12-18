"""
QUESTION:
Create a function named "nested_sum" that takes a nested list of integers as input and returns a list of integers. For each sublist in the input list, calculate the sum of its elements and check if the sum is a prime number. If the sum is a prime number, include it in the output list. The output list should only contain the prime sums of the sublists.
"""

def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def nested_sum(nested_list):
    """
    Returns the sum of values in each sublist of the nested list
    separately, but only if the sum is a prime number.
    """
    result = []
    for lst in nested_list:
        sum_lst = sum(lst)
        if is_prime(sum_lst):
            result.append(sum_lst)
    return result