"""
QUESTION:
Given a series with starting 6 members of the series. Given an integer n find the nth term of this series modulo 10^{9}+7.
Series: 7, 15, 32, 67, 138, 281, ............
Example 1:
Input: n = 2
Output: 15
Explaination: The value is given in 
the series in question.
Your Task:
You do not need to read input or print anything.Your task is to complete the function nthTerm() which takes n as input parameter and returns the value of the nth term modulo 10^{9}+7.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 120
"""

def nth_term(n: int) -> int:
    if n == 1:
        return 7
    
    s = 7
    m = 10**9 + 7
    
    for i in range(2, n + 1):
        s = (s * 2 + (i - 1)) % m
    
    return s