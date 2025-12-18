"""
QUESTION:
Write a function called `find_unique_prime_combinations` that takes a list of integers as input and returns a set of all unique combinations of size three in the list that are prime numbers. The input list will contain at least 10 elements and will not exceed 100 elements, and the function should have a time complexity no greater than O(n^3), where n is the number of elements in the list.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_unique_prime_combinations(numbers):
    combinations = set()
    n = len(numbers)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                combination = [numbers[i], numbers[j], numbers[k]]
                if all(map(is_prime, combination)):
                    combinations.add(tuple(combination))
    return combinations