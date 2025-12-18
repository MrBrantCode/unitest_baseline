"""
QUESTION:
Given a number N.Find the minimum sum of its factors.
Example 1:
Input:
N=10
Output:
7
Explanation:
There are two ways to factories N, which are
10=1*10(sum=10+1=11)
10=2*5(sum=2+5=7)
Thus, the answer is 7.
Example 2:
Input:
N=12
Output:
7
Explanation:
There are  ways to factorise N, which are
12=12*1(sum=12+1=13)
12=3*4(sum=3+4=7)
12=6*2(sum=6+2=8)
12=2*3*2(sum=2+3+2=7).
Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfFactors() which takes a number N as an input parameter and returns the minimum sum of its factors.
Expected Time Complexity:O(N^{1/2})
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{5}
"""

def minimum_sum_of_factors(N):
    if N <= 2:
        return 1
    
    p = N
    k = int(N ** 0.5)
    s = 0
    
    for i in range(2, k + 1):
        while N % i == 0:
            s += i
            N = N // i
    
    if s == 0:
        return p + 1
    
    if N != 1:
        return s + N
    
    return s