"""
QUESTION:
Create a function named `get_sum_of_first_and_last` that takes a list of lists as input, where each inner list contains integers. The function should return a list of tuples, where each tuple contains the first and last elements of an inner list, and their sum is a prime number. The function should skip inner lists with only one element and return an empty list if no valid tuples are found. The time complexity of the function should be O(n), where n is the total number of elements in the inner lists.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_sum_of_first_and_last(numbers):
    result = []
    for lst in numbers:
        if len(lst) == 1:
            continue
        first = lst[0]
        last = lst[-1]
        total = first + last
        if is_prime(total):
            result.append((first, last))
    return result