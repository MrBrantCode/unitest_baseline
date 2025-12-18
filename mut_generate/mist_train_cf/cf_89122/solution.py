"""
QUESTION:
Create a function named `filter_primes` that takes a list of integers as input, filters out the prime numbers, and returns them in a new list. The input list will contain integers in the range of -1000 to 1000. The function should have a time complexity of O(n√m) and a space complexity of O(1), excluding the space required to store the filtered numbers in the new list. The function should not use any built-in functions or libraries that directly solve the problem and should handle edge cases such as when the input list is empty or contains only negative numbers.
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