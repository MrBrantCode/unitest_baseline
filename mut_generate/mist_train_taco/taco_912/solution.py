"""
QUESTION:
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string that reads the same backward. More formally, S is a palindrome if reverse(S) = S. In case of conflict, return the substring which occurs first ( with the least starting index).
Example 1:
Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
Example 2:
Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestPalin() which takes the string S as input and returns the longest palindromic substring of S.
Expected Time Complexity: O(|S|^{2}).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ |S| ≤ 10^{3}
"""

def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    r = s[::-1]
    
    # If the entire string is a palindrome, return it
    if r == s:
        return s
    
    # If the string length is 1, return the string itself
    elif n == 1:
        return s
    
    # Iterate over possible lengths of substrings from longest to shortest
    for i in range(n, 0, -1):
        for j in range(n - i + 1):
            h = s[j:i + j]
            if h == h[::-1]:
                return h