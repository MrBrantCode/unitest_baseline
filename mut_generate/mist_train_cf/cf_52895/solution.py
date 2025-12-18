"""
QUESTION:
Write a function named `check_array` that takes an array as input and returns a string indicating whether the length of the array is a prime number or a composite number. The function should return "Prime number of elements" if the length is a prime number, and "Composite number of elements" otherwise.
"""

def is_prime(n):
    """ Function to check if a number is prime """
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def check_array(array):
    """ Function to check if the length of an array is a prime number """
    length = len(array)
    if is_prime(length):
        return "Prime number of elements"
    else:
        return "Composite number of elements"