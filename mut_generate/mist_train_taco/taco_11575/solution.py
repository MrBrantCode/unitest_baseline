"""
QUESTION:
Furik loves writing all sorts of problems, especially such that he can't solve himself. You've got one of his problems, the one Furik gave to Rubik. And Rubik asks you to solve it.

There is integer n and array a, consisting of ten integers, indexed by numbers from 0 to 9. Your task is to count the number of positive integers with the following properties:

  * the number's length does not exceed n; 
  * the number doesn't have leading zeroes; 
  * digit i (0 ≤ i ≤ 9) occurs in the number at least a[i] times. 

Input

The first line contains integer n (1 ≤ n ≤ 100). The next line contains 10 integers a[0], a[1], ..., a[9] (0 ≤ a[i] ≤ 100) — elements of array a. The numbers are separated by spaces.

Output

On a single line print the remainder of dividing the answer to the problem by 1000000007 (109 + 7).

Examples

Input

1
0 0 0 0 0 0 0 0 0 1


Output

1


Input

2
1 1 0 0 0 0 0 0 0 0


Output

1


Input

3
1 1 0 0 0 0 0 0 0 0


Output

36

Note

In the first sample number 9 meets the requirements.

In the second sample number 10 meets the requirements.

In the third sample numbers 10, 110, 210, 120, 103 meet the requirements. There are other suitable numbers, 36 in total.
"""

from math import factorial

def count_valid_numbers(n, a):
    dp = [[-1 for _ in range(101)] for _ in range(101)]
    hell = 1000000007
    
    def solve(n, p, a):
        if dp[n][p] != -1:
            return dp[n][p]
        elif p == 9:
            if n >= a[9]:
                return 1
            else:
                return 0
        elif p == 0:
            ans = 0
            for i in range(a[0], n):
                z = solve(n - i, 1, a)
                z *= factorial(n - 1)
                z //= factorial(i)
                z //= factorial(n - 1 - i)
                ans += z
            dp[n][p] = ans
            return ans
        else:
            ans = 0
            for i in range(a[p], n + 1):
                z = solve(n - i, p + 1, a)
                z *= factorial(n)
                z //= factorial(i)
                z //= factorial(n - i)
                ans += z
            dp[n][p] = ans
            return ans
    
    ans = 0
    for i in range(1, n + 1):
        ans += solve(i, 0, a)
        ans %= hell
    return ans