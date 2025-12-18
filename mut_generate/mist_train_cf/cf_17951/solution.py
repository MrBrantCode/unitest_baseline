"""
QUESTION:
Write a function named `factorial`, `sum_of_digits`, and `product_of_digits` that takes an integer `n` (1 <= n <= 20) as input and returns its factorial, the sum of all the digits in the factorial, and the product of all the digits in the factorial, respectively. The functions should have a time complexity of O(n) and a space complexity of O(1).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def product_of_digits(number):
    product = 1
    while number > 0:
        product *= number % 10
        number //= 10
    return product