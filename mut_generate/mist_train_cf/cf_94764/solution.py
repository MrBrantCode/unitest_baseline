"""
QUESTION:
Create a function named `print_prime_elements` that takes a 2-dimensional array as input and prints the elements where the sum of their row and column indices is a prime number. Do not use any built-in functions or libraries to determine if a number is prime. The input array is a list of lists where each inner list has the same number of elements.
"""

def print_prime_elements(arr):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    rows = len(arr)
    cols = len(arr[0])

    for i in range(rows):
        for j in range(cols):
            if is_prime(i + j):
                print(arr[i][j])