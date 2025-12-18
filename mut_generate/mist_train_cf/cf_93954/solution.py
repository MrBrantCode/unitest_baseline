"""
QUESTION:
Create a function `generate_array()` that generates a 2D NumPy array with the following properties: 
- the total number of elements is a multiple of 5
- the array has 5 columns
- the sum of each row is a prime number
- the product of each column is a perfect square
- the array should be as small as possible while meeting the above conditions
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
        arr[i, :] = prime_numbers[i]

    for j in range(arr.shape[1]):
        arr[:, j] = perfect_squares[j]

    return arr