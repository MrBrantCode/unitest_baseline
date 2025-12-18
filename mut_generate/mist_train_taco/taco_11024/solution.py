"""
QUESTION:
Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.
Example 1:
Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
Example 2:
Input:
A = 3, B = 2
str1 = ABC
str2 = AC
Output: 2
Explanation: LCS of "ABC" and "AC" is
"AC" of length 2.
Your Task:
Complete the function lcs() which takes the length of two strings respectively and two strings as input parameters and returns the length of the longest subsequence present in both of them. 
Expected Time Complexity : O(|str1|*|str2|)
Expected Auxiliary Space: O(|str1|*|str2|)
Constraints:
1<=size(str1),size(str2)<=10^{3}
"""

def longest_common_subsequence(str1: str, str2: str) -> int:
    x = len(str1)
    y = len(str2)
    
    # Create a 2D list to store lengths of longest common subsequence
    l = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
    
    # Build the l[x][y] in bottom-up fashion
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if str1[i - 1] == str2[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    
    # The length of the longest common subsequence is stored in l[x][y]
    return l[x][y]