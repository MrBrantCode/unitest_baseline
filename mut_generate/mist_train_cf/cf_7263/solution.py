"""
QUESTION:
Create a function called `sum_fibonacci` that calculates the sum of the first `n` Fibonacci numbers. The function should take an integer `n` and an optional boolean `even` as arguments, where `n` is a prime number and `even` is a flag to calculate the sum of even Fibonacci numbers instead of all Fibonacci numbers. The function should use a caching mechanism to store previously calculated Fibonacci numbers to optimize performance. If `even` is `True`, the function should only calculate the sum of even Fibonacci numbers up to `n`. The time complexity of the function should not exceed O(n), where n is the input number.
"""

def sum_fibonacci(n, even=False):
    """
    Calculate the sum of the first n Fibonacci numbers.

    Args:
    n (int): A prime number.
    even (bool, optional): Flag to calculate the sum of even Fibonacci numbers. Defaults to False.

    Returns:
    int: The sum of the Fibonacci numbers.

    """
    cache = {}
    def fibonacci(k):
        """
        Calculate the kth Fibonacci number using caching.

        Args:
        k (int): The position of the Fibonacci number.

        Returns:
        int: The kth Fibonacci number.

        """
        if k in cache:
            return cache[k]
        if k <= 1:
            return k
        else:
            fib = fibonacci(k-1) + fibonacci(k-2)
            cache[k] = fib
            return fib

    if even:
        fib_sum = 0
        i = 1
        while True:
            fib = fibonacci(i)
            if fib > n:
                break
            if fib % 2 == 0:
                fib_sum += fib
            i += 1
        return fib_sum
    else:
        fib_sum = 0
        for i in range(1, n+1):
            fib_sum += fibonacci(i)
        return fib_sum