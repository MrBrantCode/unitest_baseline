"""
QUESTION:
Create a function `fib_like_invert(n)` that generates a Fibonacci-like sequence of `n` terms with alternating 0s and 1s, where the pattern inverts (1s become 0s and 0s become 1s) whenever the sequence reaches a prime number, and then resets after each prime number.
"""

def fib_like_invert(n):
    def check_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if n < 0:
        return "Input should be non-negative"
    else:
        res = [0, 1]
        invert = False
        for i in range(2, n):
            res.append(res[i - 2] ^ 1 if not invert else res[i - 2])
            if check_prime(res[-1]):
                invert = not invert  # invert pattern
        return res[:n]