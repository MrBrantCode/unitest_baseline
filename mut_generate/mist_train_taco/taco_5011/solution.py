"""
QUESTION:
Given a positive integer n. The task is to check whether this integer has an alternate pattern of 0 and 1 in its binary representation or not.
NOTE: Return 1 if the integer has alternate 0 and 1 in its binary representation else return 0. 
Example 1:
Input: n = 12
Output: 0 
Explanation: n = 12 = "1100" 
Hence there is no alternate pattern.
Example 2:
Input: n = 10
Output: 1
Explanation: n = 10 = "1010".
Hence n has an alternate pattern.
Your Task:  
You dont need to read input or print anything. Complete the function bitsAreInAltOrder() which takes n as input parameter and returns 1 if the integer has alternate 0 and 1 in its binary representation else return 0.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10^{15}
"""

def bits_are_in_alt_order(n: int) -> int:
    s = bin(n)
    for i in range(3, len(s)):
        if s[i] == s[i - 1]:
            return 0
    return 1