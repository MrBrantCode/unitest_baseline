"""
QUESTION:
Create two functions: `fib(n)` and `fib_even_sum(n)`. 

`fib(n)` should calculate and return an array of the Fibonacci series containing numbers less than or equal to `n`. 

`fib_even_sum(n)` should use `fib(n)` to compute the sum of even numbers only in the Fibonacci series less than or equal to `n`.
"""

def entance(n):
    def fib(n):
        """Return the Fibonacci series up to n."""
        result = []
        a, b = 0, 1
        while a <= n:
            result.append(a)
            a, b = b, a+b
        return result

    """Return the sum of even Fibonacci numbers up to n."""
    fib_nums = fib(n)
    even_sum = sum(x for x in fib_nums if x % 2 == 0)
    return even_sum