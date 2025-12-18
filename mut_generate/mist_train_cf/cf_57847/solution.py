"""
QUESTION:
Write a function `multiply_abs_values_v3` that takes a list of float numbers as input and returns the product of their absolute values, rounded down to the nearest integers, excluding any elements divisible by prime numbers less than 10. Negative values with a decimal component of 0.5 or greater should be treated as positive. The function should also recognize -0 and 0 as distinct values.
"""

def multiply_abs_values_v3(lst):
    product = 1
    primes_less_than_10 = [2, 3, 5, 7]
    check_zero = str(lst).count("-0")
    
    for num in lst:
        num = round(abs(num)) if abs(num) % 1 >= 0.5 else int(abs(num))
        if num != 0 and all(num % i != 0 for i in primes_less_than_10):
            product *= num

    for i in range(check_zero):
        product *= -1
        
    return product