"""
QUESTION:
Write a function named `print_elements_if_prime` that takes a 2-dimensional array `arr` as input. The function should print the elements of the array where the sum of the row index and column index is a prime number.
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