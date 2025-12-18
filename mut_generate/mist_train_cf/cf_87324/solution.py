"""
QUESTION:
Create a function `prime_list(lst)` that takes a list of integers as input and returns a list of prime numbers from the input list. The output list should be sorted in descending order and should not contain any duplicate values. Do not use built-in sorting or duplicate removal functions. The function should be able to handle large lists efficiently and should not exceed a time complexity of O(n^2).
"""

def prime_list(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for x in lst:
        if is_prime(x) and (not result or x != result[-1]):
            result.append(x)
    result.sort(reverse=True)
    return result