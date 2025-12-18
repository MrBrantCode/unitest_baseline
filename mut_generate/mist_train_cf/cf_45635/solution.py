"""
QUESTION:
Write a function `compare_values(n1, n2)` that takes two integers `n1` and `n2` as input, calculates the sum and product of their divisors, and returns `True` if the sum and product of divisors of `n1` equals the sum and product of divisors of `n2`, and `False` otherwise. The function should consider all divisors, including the numbers themselves.
"""

def find_divisors(n):
    divisors = [i for i in range(1,n+1) if n%i==0] 
    return divisors

def calc_values(n):
    divisors = find_divisors(n)
    sum_divisors = sum(divisors)
    product_divisors = 1
    for i in divisors:
        product_divisors *= i
    return (sum_divisors, product_divisors)

def compare_values(n1,n2):
    sum1, product1 = calc_values(n1)
    sum2, product2 = calc_values(n2)
    return (sum1 == sum2 and product1 == product2)