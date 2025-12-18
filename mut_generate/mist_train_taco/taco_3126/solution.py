"""
QUESTION:
Given string s and an integer, you have to transform s into a palindrome. In order to achieve that you have to perform exactly k insertion of characters(you cannot perform anymore or less number of insertions). The task is to check if the string can be converted to a palindrome by making exactly k insertions.
Example 1:
Input: s = "abac", K = 2
Output: 1
Explanation: "abac" can be transformed to 
"cabbac" (which is palindrome) adding 
two characters c and b.
Example 2:
Input: s = "abcde", K = 3
Output: 0
Explanation: "abcde" cannot be transformed
to palindrome using 3 insertions.
Your Task:  
You don't need to read input or print anything. Complete the function isPossiblePalindrome() which takes s and K as input parameters and returns a boolean value
Expected Time Complexity: O(|s|^{2})
Expected Auxiliary Space: O(|s|^{2})
Constraints:
1 ≤ |s| ≤ 103
s contains lower case English alphabets
"""

def is_possible_palindrome(s: str, K: int) -> bool:
    n = len(s)
    s1 = s
    s2 = s[::-1]
    t = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                t[i][j] = 1 + t[i - 1][j - 1]
            else:
                t[i][j] = max(t[i - 1][j], t[i][j - 1])
    
    return n - t[-1][-1] <= K