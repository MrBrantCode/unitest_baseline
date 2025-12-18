"""
QUESTION:
Ishaan is playing with strings these days. He has found a new string. He wants to modify it as per the following rules to make it valid:
	The string should not have three consecutive same characters (Refer example for explanation).
	He can add any number of characters anywhere in the string. 
Find the minimum number of characters which Ishaan must insert in the string to make it valid.
Example 1:
Input:
S = aabbbcc
Output: 1
Explanation: In aabbbcc 3 b's occur
consecutively, we add a 'd',and Hence,
output will be aabbdbcc.
Example 1:
Input:
S = aaaaa
Output: 2
Explanation:  In aaaaa 5 a's occur
consecutively,we need to add 2 'b', and
Hence, the output will be aababaa.
Your Task:
This is a function problem. You only need to complete the function modified() that returns the answer.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints : 
1 <= Length of S <= 10^{5}
"""

def min_insertions_to_avoid_three_consecutive(s: str) -> int:
    i = 2
    res = 0
    while i < len(s):
        if s[i] == s[i - 1] == s[i - 2]:
            res += 1
            i += 2
        else:
            i += 1
    return res