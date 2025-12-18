"""
QUESTION:
Implement a recursive function `fibonacci(n, a, b)` that prints the Fibonacci sequence up to the nth term. The function should have the following properties: 
- Take three parameters: `n` (the current term number), `a` (the previous term), and `b` (the current term). 
- Have a time complexity of O(n), where n is the input term number. 
- Not use any loops or temporary variables.
- Use default values of 0 and 1 for `a` and `b` respectively when calling the function.
"""

def fibonacci(n, a=0, b=1):
    if n == 0:
        return
    else:
        print(a)
        fibonacci(n-1, b, a+b)