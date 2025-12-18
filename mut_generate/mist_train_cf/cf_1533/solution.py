"""
QUESTION:
Implement a function `fibonacci(n)` to generate the nth element in a Fibonacci series, where n is an integer. The function should have a time complexity of O(log n) and a space complexity of O(log n). The function should use memoization and be able to handle negative values of n.
"""

def fibonacci(n):
    memo = {}

    def fibMemo(n, memo):
        if n in memo:
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo)
        return memo[n]

    if n < 0:
        if n % 2 == 0:
            return -fibMemo(abs(n), memo)
        else:
            return fibMemo(abs(n), memo)
    else:
        return fibMemo(n, memo)