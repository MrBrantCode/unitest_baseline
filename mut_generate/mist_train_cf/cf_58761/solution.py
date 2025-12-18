"""
QUESTION:
Design a function `array_length_check` that takes an array as input and determines whether the length of the array is a prime or composite number. The function should return a message indicating whether the length is prime or composite. The array can contain any number of elements, and the function should be able to handle arrays of various lengths.
"""

def array_length_check(array):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    length = len(array)
    if is_prime(length):
        return "The length of the array is a prime number."
    else:
        return "The length of the array is a composite number."