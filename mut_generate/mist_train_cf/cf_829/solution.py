"""
QUESTION:
Write a Python function `calculate_lcm(numbers)` that calculates the least common multiple (LCM) of a list of integers. The function should take a list of integers as input and return the LCM of all the numbers in the list. The time complexity of the function should be O(n^2 log n), where n is the length of the input list.
"""

import math

def calculate_lcm(numbers):
    def find_prime_factors(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n = n / 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n = n / i
        if n > 2:
            factors.append(n)
        return factors
    
    prime_factors = []
    max_occurrences = {}
    for number in numbers:
        factors = find_prime_factors(number)
        prime_factors.append(factors)
        occurrences = {}
        for factor in factors:
            if factor in occurrences:
                occurrences[factor] += 1
            else:
                occurrences[factor] = 1
        for factor, occurrence in occurrences.items():
            if factor in max_occurrences:
                max_occurrences[factor] = max(max_occurrences[factor], occurrence)
            else:
                max_occurrences[factor] = occurrence
    
    lcm = 1
    for factor, occurrence in max_occurrences.items():
        lcm *= factor ** occurrence
    
    return lcm