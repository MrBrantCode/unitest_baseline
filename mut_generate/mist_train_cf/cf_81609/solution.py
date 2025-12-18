"""
QUESTION:
Create a function called `check_prime_and_even` that takes a list of integers as input and returns a new list containing all numbers from the input list that are both even and prime. The function should be efficient and handle large lists of numbers. Note that the output list is expected to contain at most one element, as there is only one even prime number, which is 2.
"""

def check_prime_and_even(numbers):
    def check_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        sqrtn = int(n**0.5)+1
        for divisor in range(3, sqrtn, 2):
            if n % divisor == 0:
                return False
        return True

    return [num for num in numbers if num % 2 == 0 and check_prime(num)]