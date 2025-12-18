"""
QUESTION:
Given a string S which only contains lowercase alphabets. Find the length of the longest substring of S such that the characters in it can be rearranged to form a palindrome. 
Example 1:
Input:
S = "aabe"
Output:
3
Explanation:
The substring "aab" can be rearranged to
"aba" which is the longest palindrome
possible for this String.
Example 2:
Input:
S = "adbabd"
Output:
6
Explanation:
The whole string “adbabd” can be
rearranged to form a palindromic substring.
One possible arrangement is "abddba".
Thus, output length of the string is 6. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function longestSubstring() which takes a String S as input and returns the length of largest possible Palindrome.
Expected Time Complexity: O(|S|*26)
Expected Auxiliary Space: O(|S|*26)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def longest_palindromic_substring_length(s: str) -> int:
    ans = 1
    l = len(s)
    f = {0: -1}
    x = 0
    for i in range(l):
        z = ord(s[i]) - 97
        x = x ^ 1 << z
        if x in f:
            ans = max(ans, i - f[x])
        for j in range(26):
            t = x ^ 1 << j
            if t in f:
                ans = max(ans, i - f[t])
        if x not in f:
            f[x] = i
    return ans