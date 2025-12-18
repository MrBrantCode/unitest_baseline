"""
QUESTION:
Implement the `fibonacci` function to generate the nth element in a Fibonacci series. The function should take a single integer `n` as input and return the corresponding Fibonacci number. The function must have a time complexity of O(log n) and a space complexity of O(log n). It should handle both positive and negative values of `n` and return the corresponding Fibonacci element.
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