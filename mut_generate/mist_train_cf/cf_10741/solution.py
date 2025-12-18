"""
QUESTION:
Create a function `print_elements_if_prime` that takes a 2D array as input and prints the elements where the sum of the row index and column index is a prime number. The function should handle arrays of any size.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_elements_if_prime(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if is_prime(i + j):
                print(arr[i][j])