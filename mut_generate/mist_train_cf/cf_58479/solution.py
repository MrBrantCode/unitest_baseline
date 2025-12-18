"""
QUESTION:
Create a function `check_array` that takes an array as input and prints whether the length of the array is a prime or composite number. The function should use a helper function `is_prime` to determine if a number is prime.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_array(arr):
    length = len(arr)
    if is_prime(length):
        print("Length of the array is a prime number")
    else:
        print("Length of the array is a composite number")