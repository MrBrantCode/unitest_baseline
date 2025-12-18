"""
QUESTION:
Write a function `sum_elements_fibonacci` that takes two parameters, `b` and `a`, where `b` is a positive integer representing the position in the Fibonacci sequence to start from and `a` is an integer less than 1000. The function should return `True` if `a` is the sum of three consecutive Fibonacci numbers starting from position `b` and `False` otherwise.
"""

def sum_elements_fibonacci(b, a):
    fib_nums = [0,1]
    for i in range(2,a+1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    if b > len(fib_nums)-3:
        return False
    for i in range(b-1, len(fib_nums)-2):
        if fib_nums[i] + fib_nums[i+1] + fib_nums[i+2] == a:
            return True
    return False