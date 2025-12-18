"""
QUESTION:
You are given a number N. Your task is to determine if N is an amazing number or not.  A number is called amazing if it has exactly three distinct divisors.
Example 1:
Input: N = 3
Output: 0 
Explanation: 3 has only two divisors
1 and 3.So answer is 0.
Example 2:
Input: N = 4
Output: 1
Explanation: 4 has Exactly Three divisors
1, 2 and 4.So answer is 1. 
Your Task:  
You dont need to read input or print anything. Complete the function isAmazing() which takes N as input parameter and returns 1 if N is an amazing number else return 0.
Expected Time Complexity: O(N^{1/4})
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=10^{18}
"""

def is_amazing(n: int) -> int:
    c = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            c += 1
            if i != n // i:
                c += 1
        if c > 3:
            break
        i += 1
    return 1 if c == 3 else 0