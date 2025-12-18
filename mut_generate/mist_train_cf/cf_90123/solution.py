"""
QUESTION:
Write a function `my_recursive_function` that takes a variable `my_var` as input and calls itself recursively with `my_var + 1` until `my_var` is a prime number. The function should return the prime number and have a time complexity of O(n), where n is the number of recursive calls, and a space complexity of O(log n), where n is the value of `my_var`.
"""

def my_recursive_function(my_var):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if is_prime(my_var):
        return my_var
    else:
        return my_recursive_function(my_var + 1)