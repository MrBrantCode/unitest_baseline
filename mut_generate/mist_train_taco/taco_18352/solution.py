"""
QUESTION:
Given string s consisting only a,b,c. return the number of substrings containing at least one occurrence of all these characters a, b, and c.
Example 1:
Input:
abcabc
Output:
10
Explanation:
The required substrings  are "abc", "abca", "abcab", "abcabc",
"bca", "bcab", "bcabc", "cab", "cabc" and "abc".
Example 2:
Input:
aaacb
Output:
3
Your Task:
You don't have to read input or print anything. Your task is to complete the function countSubstring() which takes the string s and returns the count of substring having at least a,b,c.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)
Constraint:
3<=s.length<=5 x 10^{4  }
S only contains a,b,c.
"""

def count_substrings_with_all_chars(s: str) -> int:
    n = len(s)
    j = 0
    (a, b, c) = (0, 0, 0)
    ans = 0
    
    for i in range(n):
        if s[i] == 'a':
            a += 1
        elif s[i] == 'b':
            b += 1
        else:
            c += 1
        
        while a > 0 and b > 0 and c > 0:
            ans += n - i
            if s[j] == 'a':
                a -= 1
            elif s[j] == 'b':
                b -= 1
            else:
                c -= 1
            j += 1
    
    return ans