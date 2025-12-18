"""
QUESTION:
Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.
Example 1:
Input:
N = 5
Output: 1 1 2 3 5
Example 2:
Input:
N = 7
Output: 1 1 2 3 5 8 13
Your Task:
Your task is to complete printFibb() which takes single argument N and returns a list of first N Fibonacci numbers.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Note: This space is used to store and return the answer for printing purpose.
Constraints:
1<= N <=84
"""

def generate_fibonacci(N: int) -> list[int]:
    if N <= 0:
        return []
    
    result = [0] * N
    f1, f2 = 1, 1
    
    if N >= 1:
        result[0] = f1
    if N >= 2:
        result[1] = f2
    
    for i in range(2, N):
        f = f1 + f2
        f2 = f1
        f1 = f
        result[i] = f
    
    return result