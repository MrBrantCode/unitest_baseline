"""
QUESTION:
Create a function named `generate_array()` that returns a 2D NumPy array with all elements initially set to 0. The size of the array must be a multiple of 5 and it must be reshaped into a 2D array with exactly 5 columns. The function should then modify the array such that the sum of each row equals a prime number and the product of each column equals a perfect square.
"""

import numpy as np

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect_square(num):
    if num < 0:
        return False
    root = int(num ** 0.5)
    return root * root == num

def generate_array():
    array_size = 20
    prime_numbers = [num for num in range(2, 100) if is_prime(num)]
    perfect_squares = [num * num for num in range(100)]
    arr = np.zeros(array_size)
    arr = arr.reshape(-1, 5)
    
    for i in range(arr.shape[0]):
        arr[i, :] = prime_numbers[i % len(prime_numbers)]
        
    for j in range(arr.shape[1]):
        arr[:, j] = [perfect_squares[j % len(perfect_squares)] for _ in range(arr.shape[0])]
    
    return arr