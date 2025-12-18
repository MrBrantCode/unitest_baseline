"""
QUESTION:
Write a program which prints $n$-th fibonacci number for a given integer $n$. The $n$-th fibonacci number is defined by the following recursive formula:

\begin{equation*} fib(n)= \left \\{ \begin{array}{ll} 1 & (n = 0) \\\ 1 & (n = 1) \\\ fib(n - 1) + fib(n - 2) & \\\ \end{array} \right. \end{equation*}

Constraints

* $0 \leq n \leq 44$

Input

An integer $n$ is given.

Example

Input

3


Output

3
"""

def fibonacci(n: int) -> int:
    if n < 0 or n > 44:
        raise ValueError("Input n must be between 0 and 44 inclusive.")
    
    if n == 0 or n == 1:
        return 1
    
    num = [1, 1]
    for i in range(2, n + 1):
        f = num[i - 1] + num[i - 2]
        num.append(f)
    
    return num[n]