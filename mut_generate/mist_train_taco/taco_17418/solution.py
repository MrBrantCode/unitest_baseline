"""
QUESTION:
Given a string S, Check if characters of the given string can be rearranged to form a palindrome.
Note: You have to return 1 if it is possible to convert the given string into palindrome else return 0. 
Example 1:
Input:
S = "geeksogeeks"
Output: Yes
Explanation: The string can be converted
into a palindrome: geeksoskeeg
Example 2:
Input: 
S = "geeksforgeeks"
Output: No
Explanation: The given string can't be
converted into a palindrome.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPossible() which takes the string S as input and returns 1 if the string can be converted into a palindrome. Else, it returns 0.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(Distinct Characters).
Constraints:
1 <= |S| <= 10^{6}
"""

def can_form_palindrome(S: str) -> int:
    char_count = {}
    
    # Count the frequency of each character in the string
    for char in S:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Count the number of characters with odd frequencies
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
    
    # A string can be rearranged into a palindrome if there is at most one character with an odd frequency
    if odd_count > 1:
        return 0
    return 1