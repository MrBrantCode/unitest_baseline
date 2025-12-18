"""
QUESTION:
Write a function named `print_prime_numbers_2d_array` that takes a 2D array as input and prints all prime numbers found in the array. The function must handle edge cases, including null values, empty arrays, and non-integer values. Use a while loop to traverse the 2D array.
"""

def check_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))

def print_prime_numbers_2d_array(array_2d):
    if array_2d is None:
        print("Array is null")
        return
    if not array_2d:
        print("Array is empty")
        return
    for row in array_2d:
        for elem in row:
            if isinstance(elem, int) and check_prime(elem):
                print(elem)