"""
QUESTION:
Write a function `last_ten_digits_of_product` to find the last ten digits of the product of all positive integers `m` less than `10^15` such that the product of the cubes of the digits (in base 10) of `m` is a perfect cube. The function should not take any arguments and return the result as an integer.
"""

MAX = 10000000000

def convert(n, base):
    s = 0
    while n > 0:
        s = s * base + n % base
        n //= base
    return s

def last_ten_digits(n):
    return n % MAX

def multiply_last_ten_digits(a, b):
    return last_ten_digits(a * b)

def last_ten_digits_of_product():
    a = [i**3 for i in range(23)]
    number_of_solutions = [0 for _ in range(10649)]
    product = [1 for _ in range(10649)]

    for i in range(1, 23):
        for j in range(a[i], 10649):
            product[j] = multiply_last_ten_digits(product[j], product[j - a[i]])
            number_of_solutions[j] += number_of_solutions[j - a[i]]
        for j in range(a[i]):
            number_of_solutions[j] = i
            product[j] = i

    result = 1
    for i in range(1, 10649):
        if number_of_solutions[i]**3 == i:
            result = multiply_last_ten_digits(result, product[i])

    return result