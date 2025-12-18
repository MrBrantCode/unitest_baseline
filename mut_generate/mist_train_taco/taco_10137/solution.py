"""
QUESTION:
You are given integer N, and return the Fibonacci Series till the Nth term.
Example:
Input:
5
Output:
0 1 1 2 3 5
Explanation:
0 1 1 2 3 5 is the Fibonacci series up to
the 5th term.(0-based indexing)
Your Task:
You don't need to read input or print anything. Your task is to complete the function Series() which takes an Integer N as input and returns a Fibonacci Series up to the Nth term.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)
Constraint:
1<=n<100
"""

def generate_fibonacci_series(N: int) -> list:
    if N == 1:
        return [0]
    elif N == 2:
        return [0, 1]
    
    series = [0, 1]
    for i in range(2, N):
        series.append(series[i - 1] + series[i - 2])
    
    return series