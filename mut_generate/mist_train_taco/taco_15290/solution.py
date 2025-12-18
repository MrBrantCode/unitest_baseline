"""
QUESTION:
Find the smallest number such that the sum of its digits is N and it is divisible by 10^{N}.
Example 1:
Input: N = 5
Outptut: 500000
Explanation: Sum of digits of 500000
is 5 and divisible by 10^{5}.
Example 2:
Input: N = 20
Output: 29900000000000000000000
Explanation: Sum of digits of 
29900000000000000000000 is 20 and
divisible by 10^{20}.
Your Task:
You don't need to read or print anything. Your task is to complete the function digitsNum() which takes the input parameter N and returns the smallest number such that sum of its digits is N and divisible by 10^{N}.
 
Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
 
Constraints:
1 <= N <= 10000
"""

def find_smallest_number(N: int) -> str:
    sum_digits = N
    digits = ''
    
    # Construct the digits part
    while sum_digits > 0:
        if sum_digits > 9:
            digits += '9'
            sum_digits -= 9
        else:
            digits += str(sum_digits)
            sum_digits = 0
    
    # Reverse the digits to get the smallest number
    digits = digits[::-1]
    
    # Append zeros to make it divisible by 10^N
    result = digits + '0' * N
    
    return result