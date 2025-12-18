"""
QUESTION:
Given an equation of the form f(n) = f(n-1) + f(n-2) where f(0) = 1, f(1) = 1 , the task is to find the n^{th} term of this sequence.
 
Example 1:
Input: n = 3
Output: 3
Explanation: f(3) = f(2) + f(1) = 3
Example 2:
Input: n = 2
Output: 2
Explanation: f(2) = f(1) + f(0) = 2
 
Yout Task:
You don't need to read or print anything. Your task is to complete the function FindNthTerm() which takes n as input parameter and returns n^{th} term mod 10^9+7 .
Expected Time Complexity: O(log(n))
Expected Space Complexity: O(K) where K is constant.
 
Constraints:
1 <= n <= 10^{9}
"""

def multiply(a, b):
    mul = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            mul[i][j] = 0
            for k in range(3):
                mul[i][j] += a[i][k] * b[k][j]
    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j] % (10**9 + 7)
    return a

def power(F, n):
    M = [[1, 1, 0], [1, 0, 0], [0, 1, 0]]
    if n == 1:
        return F[0][0] + F[0][1]
    power(F, n // 2)
    F = multiply(F, F)
    if n % 2 != 0:
        F = multiply(F, M)
    return F[0][0] + F[0][1]

def find_nth_term(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    F = [[1, 1, 0], [1, 0, 0], [0, 1, 0]]
    k = power(F, n - 1)
    return k % (10**9 + 7)