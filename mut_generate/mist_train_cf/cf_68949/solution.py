"""
QUESTION:
Write a function called `check_prime` that recognizes handwritten digits using the MNIST dataset and identifies if the number written is prime or not. The function should use Convolutional Neural Networks (CNNs) and not use any prebuilt functions to check for prime numbers. The MNIST dataset should be loaded and preprocessed accordingly. The function should be implemented from scratch and output the list of prime numbers. 

Note: The `check_prime` function should take no arguments.
"""

def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if (n % i) == 0:
                return False
        return True