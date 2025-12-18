"""
QUESTION:
Implement a function `filter_primes(numbers)` that takes a list of integers as input and returns a new list containing only the prime numbers from the input list. The input list will contain integers in the range of -1000 to 1000. The function should have a time complexity of O(n√m), where n is the length of the input list and m is the maximum value in the input list, and a space complexity of O(1), excluding the space required to store the filtered numbers in the new list.
"""

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes