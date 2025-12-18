"""
QUESTION:
Given a integer number n, find largest sum of digits in all divisors of n.
 
Example 1:
Input:
n = 12
Output:
6
Explanation:
The divisors of 6 are: 1,2,3,4,6,12.
6 is the maximum digit-sum among all divisors.
Example 2:
Input:
n = 34
Output:
8
Explanation:
The divisors of 34 are: 1,2,17,34.
8 is the maximum digit-sum among all divisors. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function getLargest() which takes an Integer n as input and returns the answer.
 
Expected Time Complexity: O(sqrt(n)*log(n))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= n <= 10^{6}
"""

from math import sqrt

def find_largest_divisor_digit_sum(n: int) -> int:
    def get_digit_sum(num: int) -> int:
        s = 0
        while num != 0:
            s += num % 10
            num = num // 10
        return s
    
    max_sum = 0
    x = int(sqrt(n))
    
    for i in range(1, x + 1):
        if n % i == 0:
            aux1 = get_digit_sum(i)
            aux2 = get_digit_sum(n // i)
            max_sum = max(max_sum, aux1, aux2)
    
    return max_sum