"""
QUESTION:
Implement a recursive function called fibonacci that calculates the nth Fibonacci number, where the Fibonacci sequence is defined as the first two numbers being 0 and 1, and each subsequent number is the sum of the previous two. The function should take an integer n as input and return the nth Fibonacci number. Use a custom data structure for memoization, and do not use any built-in data structures or loops.
"""

class Memo:
    def __init__(self):
        self.memo = {}

    def get(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            return None

    def put(self, n, value):
        self.memo[n] = value

def fibonacci(n):
    memo = Memo()
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = memo.get(n-1)
        if a is None:
            a = fibonacci(n-1)
            memo.put(n-1, a)
        b = memo.get(n-2)
        if b is None:
            b = fibonacci(n-2)
            memo.put(n-2, b)
        return a + b