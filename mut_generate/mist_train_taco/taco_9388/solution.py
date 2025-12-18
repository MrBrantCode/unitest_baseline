"""
QUESTION:
Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.
Example 1:
Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first. 
Example 2:
Input: 
S = "abcde"
Output: -1
Explanation: No repeating character present.
Your Task:
You don't need to read input or print anything. Your task is to complete the function firstRep() which takes the string S as input and returns the the first repeating character in the string. In case there's no repeating character present, return '#'.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def first_repeating_char(s: str) -> str:
    char_count = {}
    order_list = []
    
    for char in s:
        if char not in char_count:
            char_count[char] = 1
            order_list.append(char)
        else:
            char_count[char] += 1
    
    for char in order_list:
        if char_count[char] > 1:
            return char
    
    return '#'