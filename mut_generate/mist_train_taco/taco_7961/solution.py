"""
QUESTION:
Given a String s, count all special palindromic substrings of size greater than 1. A Substring is called special palindromic substring if all the characters in the substring are same or only the middle character is different for odd length. Example “aabaa” and “aaa” are special palindromic substrings and “abcba” is not a special palindromic substring.
 
Example 1:
Input: 
S = "abab"
Output: 2
Explanation: All Special Palindromic substring
             size > 1 are : "aba", "bab"
 
Example 2:
Input:
S = "aaba"
Output: 2
Explanation: All Special Palindromic substring
             size > 1 are: "aa", "aba".
 
User Task:
Your task is to complete the function CountSpecialPalindrome() which takes a single argument(string str) and returns the count of special palindromic substrings. You need not take any input or print anything.
 
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).
 
Constraints:
1 <= |S| <= 10^{5}
"""

def count_special_palindromic_substrings(s: str) -> int:
    ans = 0
    n = len(s)
    i = 1
    
    while i < n:
        j = i - 1
        
        if s[i] == s[j]:
            while i < n and s[i] == s[j]:
                i += 1
            if i - j > 1:
                ans += (i - j) * (i - j - 1) // 2
        else:
            k = i
            j = 1
            c = ' '
            while k - j >= 0 and k + j < n:
                if s[k - j] == s[k + j] and (c == ' ' or c == s[k - j]):
                    ans += 1
                    c = s[k - j]
                    j += 1
                else:
                    break
            i += 1
    
    return ans