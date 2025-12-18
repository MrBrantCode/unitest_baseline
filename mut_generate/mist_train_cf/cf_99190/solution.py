"""
QUESTION:
Implement a function named `nested_sum` that takes a nested list of integers as input and returns a list of integers representing the sum of values in each sublist, but only if the sum is a prime number. The function should return the sums of sublists separately, in the order they appear in the input list. The input list can contain sublists of varying lengths, and the function should handle this variability. The function should not modify the input list.
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