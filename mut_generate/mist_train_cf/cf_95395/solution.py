"""
QUESTION:
Write a function `find_unique_prime_combinations(numbers)` that finds all unique combinations of size three in a given list of integers `numbers` that are prime numbers, with a time complexity not greater than O(n^3), where n is the number of elements in `numbers`. The list `numbers` will contain at least 10 elements and will not exceed 100 elements. The function should return a set of unique combinations, where each combination is a tuple of three prime numbers.
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
                    combinations.add(tuple(sorted(combination)))
    return combinations