"""
QUESTION:
The function `fib4(n)` should calculate the n-th element of the Fib4 number sequence without recursion. The sequence is defined as: 
- fib4(0) = 0
- fib4(1) = 0
- fib4(2) = 2
- fib4(3) = 0
- fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n > 3. 
The solution should be efficient.
"""

def fib4(n: int) -> int:
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        cache = [0] * (n + 1)
        cache[2] = 2

        for i in range(4, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3] + cache[i - 4]
            
        return cache[n]