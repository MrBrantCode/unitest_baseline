"""
QUESTION:
Given two integers ‘n’ and ‘sum’, find the count of all n digit numbers whose sum of digits is ‘sum’. Leading 0’s are not counted as digits. 
Example 1:
Input: n = 2, sum = 2
Output: 2
Explaination: 
The 2 digit numbers are 11 and 20.
Example 2:
Input: n = 1, sum = 10
Output: -1
Explaination: 
We cannot get sum as 10 from a single digit.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countWays() which takes the value n and sum as input parameters and returns the number of possible ways modulo 10^{9}+7. If there is no possible way then it returns -1.
Expected Time Complexity: O(n*sum)
Expected Auxiliary Space: O(n*sum)
Constraints:
1 ≤ n ≤ 10^{2}
1 ≤ sum ≤ 10^{3}
"""

def count_n_digit_sum_ways(n: int, sum: int) -> int:
    if sum == 0:
        if n == 1:
            return 1
        return -1
    if n * 9 < sum:
        return -1
    
    dp = {}

    def rec(d: int, s: int) -> int:
        if d == 0:
            if s == 0:
                return 1
            return 0
        if (d, s) in dp:
            return dp[(d, s)]
        su = 0
        for i in range(10):
            su += rec(d - 1, s - i)
        dp[(d, s)] = su % 1000000007
        return su % 1000000007
    
    sum1 = 0
    for i in range(1, 10):
        sum1 = (sum1 + rec(n - 1, sum - i)) % 1000000007
    
    return sum1