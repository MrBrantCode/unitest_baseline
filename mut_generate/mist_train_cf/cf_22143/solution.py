"""
QUESTION:
Implement a function named `fibonacci` that prints the Fibonacci sequence up to the nth term. The function should be recursive, use no loops, and have a time complexity of O(n). It should take two additional parameters: the previous term and the current term, both of which are initially set to default values.
"""

def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    else:
        print(a)
        fibonacci(n-1, b, a+b)