"""
QUESTION:
Given three arrays of integers, write a function `sort_prime_numbers` that classifies each array element as a prime number or not, calculates the sum of divisors for each prime number, and returns the prime numbers sorted in descending order based on the sum of their divisors. The function should have a time complexity of O(n^2) or better and should not use any built-in functions or libraries to check for prime numbers or store intermediate results. The input arrays and their contents are to be processed as a single list of prime numbers.
"""

def sort_prime_numbers(arrays):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def sum_of_divisors(n):
        div_sum = 0
        for i in range(1, n + 1):
            if n % i == 0:
                div_sum += i
        return div_sum

    prime_numbers = [num for arr in arrays for num in arr if is_prime(num)]
    for i in range(len(prime_numbers)):
        for j in range(0, len(prime_numbers) - i - 1):
            if sum_of_divisors(prime_numbers[j]) < sum_of_divisors(prime_numbers[j + 1]):
                prime_numbers[j], prime_numbers[j + 1] = prime_numbers[j + 1], prime_numbers[j]
    return prime_numbers