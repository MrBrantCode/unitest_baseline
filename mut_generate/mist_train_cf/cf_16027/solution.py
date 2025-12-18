"""
QUESTION:
Create a function called `is_fibonacci(n)` that checks if a given integer `n` is a Fibonacci number or not. If `n` is a Fibonacci number, return a statement indicating that it is a Fibonacci number. If `n` is not a Fibonacci number, return a statement indicating that it is not a Fibonacci number and include the closest Fibonacci number that is smaller than `n`. The function should not take any additional parameters and should handle all necessary calculations internally.
"""

def is_fibonacci(n):
    def is_perfect_square(num):
        square_root = int(num ** 0.5)
        return square_root * square_root == num

    def is_fib(num):
        return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

    def find_closest_fibonacci(num):
        fib_prev, fib_curr = 0, 1
        while fib_curr <= num:
            fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
        return fib_prev

    if is_fib(n):
        return f"{n} is a Fibonacci number."
    else:
        return f"{n} is not a Fibonacci number. The closest Fibonacci number smaller than {n} is {find_closest_fibonacci(n)}."