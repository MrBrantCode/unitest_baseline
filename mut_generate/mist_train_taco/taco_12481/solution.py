"""
QUESTION:
Given the series as follows 2 2 4 8 16 512....... Identify the Nth term of the series. Answers can be very large use BigInt in Java.
Example 1:
Input: N = 1
Output: 2 
Explanation: First term of the series is 2.
Example 2:
Input: N = 2
Output: 2
Explanation: Second term of the series is 2. 
Your Task:  
You dont need to read input or print anything. Complete the function NthTerm() which takes N as input parameter and returns the Nth term of the series.
Expected Time Complexity: O(logn*logn)
Expected Auxiliary Space: O(1)
Constraints:
1<= N <=12
"""

def NthTerm(N: int) -> int:
    if N == 1:
        return 2
    if N == 2:
        return 2
    smallerOut = NthTerm(N - 2)
    if N % 2 == 0:
        return smallerOut ** 3
    else:
        return smallerOut ** 2