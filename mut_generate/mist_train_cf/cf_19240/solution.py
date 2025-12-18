"""
QUESTION:
Write a function named `calculate_elements` that takes an input list of integers. The function should calculate and print the sum of the first N-1 elements if the size of the list (N) is a prime number. If N is also a perfect square, the function should calculate and print the product of the first N-2 elements. If N is neither prime nor a perfect square, the function should print an error message.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return math.isqrt(n)**2 == n

def calculate_elements(input_list):
    N = len(input_list)
    
    if is_prime(N):
        sum_of_elements = sum(input_list[:N-1])
        print("Sum of the first", N-1, "elements:", sum_of_elements)
        
        if is_perfect_square(N):
            product_of_elements = 1
            for i in range(N-2):
                product_of_elements *= input_list[i]
            print("Product of the first", N-2, "elements:", product_of_elements)
    else:
        print("Error: N is not prime or a perfect square.")