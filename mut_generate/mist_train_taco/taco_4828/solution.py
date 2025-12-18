"""
QUESTION:
Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. If there is no non-repeating character, return '$'.
Example 1:
Input:
S = hello
Output: h
Explanation: In the given string, the
first character which is non-repeating
is h, as it appears first and there is
no other 'h' in the string.
Example 2:
Input:
S = zxvczbtxyzvy
Output: c
Explanation: In the given string, 'c' is
the character which is non-repeating. 
Your Task:
You only need to complete the function nonrepeatingCharacter() that takes string S as a parameter and returns the character. If there is no non-repeating character then return '$' .
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Note: N = |S|
Constraints:
1 <= N <= 10^{3}
"""

def find_first_non_repeating_char(S: str) -> str:
    char_count = {}
    order = []
    
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            order.append(char)
    
    for char in order:
        if char_count[char] == 1:
            return char
    
    return '$'