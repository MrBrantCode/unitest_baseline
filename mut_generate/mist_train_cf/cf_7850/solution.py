"""
QUESTION:
Write a function `my_recursive_function` that takes an integer `my_var` as input, calls itself recursively with `my_var + 1` until `my_var` is a prime number, and then returns the prime number. The time complexity should be O(n), where n is the number of recursive calls, and the space complexity should be O(log n), where n is the value of `my_var`.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def my_recursive_function(my_var):
    if is_prime(my_var):
        return my_var
    else:
        return my_recursive_function(my_var + 1)