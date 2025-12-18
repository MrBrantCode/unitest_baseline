"""
QUESTION:
Given a number N. Check whether it is divisible by the sum of its digits or not.
Example 1:
Input:
N=18
Output:
1
Explanation:
The sum of digits of 18 is 1+8=9 
which divides 18.so, answer is 1.
Example 2:
Input:
N=25
Output:
0
Explanation:
The sum of digits of 25 is 2+5=7 which does
not divide 25, so answer is 0.
Your Task:
You don't need to read input or print anything.Your task is to complete the function isDivisible() which takes the number N as input parameter and returns 1 if it is divisible by its digit sum.Otherwise,it returns 0.
Expected Time Complexity:O(LogN)
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

def is_divisible_by_digit_sum(N: int) -> int:
    s = 0
    x = N
    while N != 0:
        d = N % 10
        s = s + d
        N = N // 10
    if x % s == 0:
        return 1
    else:
        return 0