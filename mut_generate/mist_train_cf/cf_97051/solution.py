"""
QUESTION:
Write a function named `my_recursive_function` that takes a variable `my_var` and recursively calls itself, incrementing `my_var` by 1 in each call, until `my_var` is a prime number. The function should return the prime number. The solution should have a time complexity of O(n), where n is the number of recursive calls made until the condition is met.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def my_recursive_function(my_var):
    if not is_prime(my_var):
        return my_recursive_function(my_var + 1)
    return my_var