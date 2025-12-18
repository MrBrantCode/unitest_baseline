"""
QUESTION:
Create a function `is_prime_even` that checks all even numbers within a given range (start to end inclusive) to determine if they are prime even numbers. The function should take two parameters, `start` and `end`, representing the start and end of the range, and print each even number in the range along with whether it is a prime even number or not.
"""

def is_prime_even(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(start, end + 1, 2):
        if num % 2 == 0 and is_prime(num):
            print(num, "is a prime even number")
        else:
            print(num, "is not a prime even number")