"""
QUESTION:
Given a number N, the task is to find a number in the range from 1 to N such that its digit sum is maximum. If there are several such numbers, print the biggest of them.
Example 1:
Input:
N = 48
Output: 48
Explanation:
There are two numbers with maximum digit sum. 
The numbers are 48 and 39 Since 48 > 39, 
it is our answer.
 
Example 2:
Input:
N = 90
Output: 89
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMax() which takes the integer N as input parameters and returns the biggest number having the maximum sum.
Expected Time Complexity: O(M) where M is the number of digits in n.
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{18}
"""

def find_max_digit_sum(N):
    def digit_sum(num):
        s = num
        sum_digits = 0
        while s != 0:
            sum_digits += s % 10
            s = s // 10
        return sum_digits
    
    ans = N
    b = 1
    x = N
    while x > 0:
        conversion9 = (x - 1) * b + (b - 1)
        if digit_sum(ans) > digit_sum(conversion9) or (digit_sum(ans) == digit_sum(conversion9) and ans > conversion9):
            ans = ans
        else:
            ans = conversion9
        x = x // 10
        b *= 10
    return ans