"""
QUESTION:
Create a function `get_prime_numbers` that takes a list of integers as input, filters out the prime numbers, and returns them in a new list sorted in ascending order. The function should have a time complexity of O(n^2), where n is the length of the input list.
"""

def get_prime_numbers(original_list):
    primes = []
    for num in original_list:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return sorted(primes)