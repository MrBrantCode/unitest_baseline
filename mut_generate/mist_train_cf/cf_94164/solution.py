"""
QUESTION:
Create a function called `get_prime_numbers` that takes a list of integers as input and returns a new list containing all the prime numbers from the original list. Implement the primality test without using any built-in functions or libraries, and optimize the function to have a time complexity of O(n * sqrt(m)), where n is the length of the input list and m is the largest number in the list.
"""

def get_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [num for num in numbers if is_prime(num)]