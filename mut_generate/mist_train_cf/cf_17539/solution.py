"""
QUESTION:
Write a function named `print_prime_elements` that takes a 2-dimensional array as input and prints all elements where the sum of the row and column indices is a prime number. The function should not use any built-in functions or libraries to determine if a number is prime. Assume the input array is a list of lists in Python, where each inner list has the same length and represents a row in the array.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_prime_elements(arr):
    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if is_prime(i + j):
                print(arr[i][j])