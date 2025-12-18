"""
QUESTION:
Write a function called `largest_prime_and_sum` that takes a vector of integers as input. The function should return the sum of the digits of the largest prime number in the vector. If no prime number exists in the vector, the function should return `None`. Optimize the solution for both time and space complexity.
"""

def largest_prime_and_sum(input_vector):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    largest_prime = -1
    for num in input_vector:
        if num > largest_prime and is_prime(num):
            largest_prime = num
    return sum(int(digit) for digit in str(largest_prime)) if largest_prime != -1 else None