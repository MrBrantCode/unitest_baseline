"""
QUESTION:
Create a function `calculate_factorial` that takes an integer `n` as input where `1 <= n <= 20`, calculates its factorial, and returns the factorial value along with the sum of its digits, product of its digits, whether it's a palindrome, its largest prime factor, and whether the input `n` is a perfect square. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

import math

def entrance(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    digit_sum = 0
    digit_product = 1
    temp_factorial = factorial
    is_palindrome_result = True

    while temp_factorial > 0:
        digit = temp_factorial % 10
        digit_sum += digit
        digit_product *= digit
        temp_factorial //= 10

    reversed_factorial = 0
    temp_factorial = factorial
    while temp_factorial > 0:
        reversed_factorial = (reversed_factorial * 10) + (temp_factorial % 10)
        temp_factorial //= 10

    if factorial != reversed_factorial:
        is_palindrome_result = False

    largest_prime_factor = 1
    temp_factorial = factorial
    while temp_factorial % 2 == 0:
        largest_prime_factor = 2
        temp_factorial //= 2

    for i in range(3, int(math.sqrt(temp_factorial)) + 1, 2):
        while temp_factorial % i == 0:
            largest_prime_factor = i
            temp_factorial //= i

    if temp_factorial > 2:
        largest_prime_factor = temp_factorial

    is_perfect_square_result = int(math.sqrt(n))**2 == n

    return factorial, digit_sum, digit_product, is_palindrome_result, largest_prime_factor, is_perfect_square_result