"""
QUESTION:
Write a function `fibfib(n: int) -> int` that calculates the nth term of the FibFib sequence, where fibfib(0) = 0, fibfib(1) = 0, fibfib(2) = 1, and fibfib(n) is the sum of fibfib(n-1), fibfib(n-2), and fibfib(n-3). The function should be able to handle values of n up to 10,000 efficiently.
"""

def fibfib(n: int) -> int:
    if n==0: return 0
    if n==1: return 0
    if n==2: return 1
    
    fibfib = [0]*(n+1)
    fibfib[2] = 1
    
    for i in range(3, n+1):
        fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3]
    
    return fibfib[n]