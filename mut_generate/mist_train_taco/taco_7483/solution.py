"""
QUESTION:
Given a string S  and a character X, the task is to find the last index (0 based indexing) of X in string S. If no index found then the answer will be -1.
Example 1:
Input: S = "Geeks", P = 'e'
Output: 2
Explanation: Last index of 'e' 
is 2.
Example 2:
Input: S = "okiyh", P = 'z'
Output: -1
Explanation: There is no character
as 'z'.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function LastIndex() which takes the string s and character p as inputs and returns the answer.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ |S| ≤ 10^{5}
S and P contain only lower and upper case alphabets.
"""

def find_last_index(s: str, p: str) -> int:
    # Initialize the result to -1 (indicating no match found)
    last_index = -1
    
    # Iterate through the string to find the last index of the character
    for i in range(len(s)):
        if s[i] == p:
            last_index = i
    
    # Return the last index found, or -1 if no match was found
    return last_index