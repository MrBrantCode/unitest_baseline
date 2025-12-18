"""
QUESTION:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:


Input: "A man, a plan, a canal: Panama"
Output: true


Example 2:


Input: "race a car"
Output: false
"""

def is_valid_palindrome(s: str) -> bool:
    # Convert the string to lowercase and filter out non-alphanumeric characters
    cleanlist = [c for c in s.lower() if c.isalnum()]
    
    # Check if the cleaned list is equal to its reverse
    return cleanlist == cleanlist[::-1]