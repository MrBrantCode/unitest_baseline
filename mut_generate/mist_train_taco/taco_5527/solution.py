"""
QUESTION:
Given a binary string of size N, you have to return the number of substrings that have even value in its decimal form.
Note: Most significant bit is on the right end side. For example - binary representation of 6 is 011. 
Example 1:
Input:
N = 3
S = "101"
Output: 2
Explanation : 
Substrings in S: 
1, 10, 101, 0, 01, 1
Corresponding decimal values:
1, 1, 5, 0, 2, 1
There are only 2 even decimal valued 
substrings.
Example 2:
Input:
N = 5
S = "10010"
Output: 
8
Explanation:
Substrings in S:
1, 0, 0, 1, 0, 10, 00, 01, 10, 100, 
001, 010, 1001, 0010 and 10010
Corresponding decimal Values are:
1, 0, 0, 1, 0, 1, 0, 2, 1, 1, 4, 2,
9, 4 ans 9
There are 8 decimal values which are even.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function evenDecimalSubStr() which takes the string S, its size N as input parameters and returns the number of substrings that has even value in its decimal form.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ T ≤ 1000
1 ≤ N ≤ 10^{5}
"""

def evenDecimalSubStr(S, N):
    output = 0
    for i in range(N):
        if S[i] == '0':
            output += N - i
    return output