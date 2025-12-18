"""
QUESTION:
Given a string s, check if it can be rotated to form a palindrome.
Example 1:
Input:
s = aaaab
Output: 1 
Explanation: "aaaab" can be rotated to
form "aabaa" which is a palindrome.
Your Task:  
You dont need to read input or print anything. Complete the function isRotatedPalindrome() which takes a string s as input parameter and returns 1 if rotated palindrome is possible, otherwise 0.
Expected Time Complexity: O(N^{2}) where N is length of s
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= s.length() <= 10^{4}
"""

def is_rotated_palindrome(s: str) -> int:
    if len(set(s)) == len(s):
        return 0
    
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return 0
    
    return 1