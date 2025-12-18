"""
QUESTION:
Create a function called "find_largest" that takes a list of integers as input and returns the largest prime number in the list. If the list does not contain any prime numbers, the function should return -1.
"""

def find_largest(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = -1
    for num in lst:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    
    return largest_prime