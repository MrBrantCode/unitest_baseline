"""
QUESTION:
Given a string, say S, print it in reverse manner eliminating the repeated characters and spaces.
Example 1:
Input: S = "GEEKS FOR GEEKS"
Output: "SKEGROF"
Example 2:
Input: S = "I AM AWESOME"
Output: "EMOSWAI"
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseString() which takes a string S as input parameter and returns a modified string. 
Expected Time Complexity: O(|S|), where |S| denotes length of string.
Expected Auxiliary Space: O(1).
"""

def reverse_string_without_duplicates(s: str) -> str:
    result = ''
    s_reverse = s[::-1]
    for char in s_reverse:
        if char == ' ':
            continue
        elif char not in result:
            result += char
    return result