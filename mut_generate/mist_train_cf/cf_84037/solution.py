"""
QUESTION:
Create a function called `fibonacci` that calculates the nth Fibonacci number within a specified range. The function should take two parameters, `n` and a range defined by `low` and `high`. The Fibonacci sequence starts with 0 and 1, and each subsequent number is obtained by adding the previous two. The function should return the nth Fibonacci number if it falls within the specified range; otherwise, it should return a message indicating that the number is out of range.
"""

def fibonacci(n, low, high):
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        fib_n = fib_list[-1]
        
    if low <= fib_n <= high:
        return fib_n
    else:
        return f"The {n}th Fibonacci number is out of range."