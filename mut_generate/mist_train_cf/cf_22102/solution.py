"""
QUESTION:
Write a function named `sum_of_primes` that takes an array of integers and returns the sum of the prime numbers in the array. Consider only positive integers greater than 1 as prime numbers and use an efficient prime number checking algorithm. The input array can contain duplicate values and non-prime numbers. The function should handle arrays of any length and should not take any other parameters besides the input array.
"""

def sum_of_primes(input_array):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in input_array if is_prime(num))