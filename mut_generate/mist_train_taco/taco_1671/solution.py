"""
QUESTION:
Given a positive integer N, find the number of factors in N! ( N factorial).
Example :
Input:
N = 5
Output:
16
Explanation:
5! is 120 and the number of factors of
120 are 1 2 3 4 5 6 8 10 12 15 20 24 30
40 60 120 So the number of factors are 16.
Example 2:
Input:
N = 4
Output:
8
Explanation:
4! is 24 and the number of factors of
24 are 1 2 3 4 6 8 12 24
So the number of factors are 8.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function factorsOfFactorial() which takes an integer N as an input parameter and return the number of factors of N factorial.
Expected Time Complexity: O(NLogLogN)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 100
"""

def factors_of_factorial(N: int) -> int:
    if N < 1:
        return 1
    
    def cal_ways(n: int, p: int) -> int:
        j = p
        c = 0
        while n // j > 0:
            c += n // j
            j *= p
        return c + 1
    
    t = N
    N = N + 1
    r = 1
    prime = [1] * N
    prime[0] = 0
    prime[1] = 0
    
    for i in range(2, int(N ** 0.5) + 1):
        j = 2
        while j * i < N:
            prime[j * i] = 0
            j += 1
    
    for i in range(len(prime)):
        if prime[i] == 1:
            r *= cal_ways(t, i)
    
    return r