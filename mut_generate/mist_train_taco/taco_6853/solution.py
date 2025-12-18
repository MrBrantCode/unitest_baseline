"""
QUESTION:
Given a string, your task is to reverse the string keeping the spaces intact to their positions.
Example 1:
Input:
S = "Help others"
Output: sreh topleH
Explanation: The space is intact at index 4
while all other characters are reversed.
Example 2:
Input: 
S = "geeksforgeeks"
Output: skeegrofskeeg
Explanation: No space present, hence the
entire string is reversed.
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverseWithSpacesIntact() which takes the string S as input and returns the resultant string by reversing the string while keeping all the spaces intact.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def reverse_with_spaces_intact(s: str) -> str:
    # List to store the indices of spaces
    space_indices = []
    
    # Collect all the indices of spaces in the original string
    for i in range(len(s)):
        if s[i] == ' ':
            space_indices.append(i)
    
    # Reverse the string without spaces
    reversed_string = s[::-1].replace(' ', '')
    
    # If there are no spaces, return the reversed string directly
    if not space_indices:
        return reversed_string
    
    # Insert spaces back into their original positions
    j = 0
    for i in range(len(reversed_string) + len(space_indices)):
        if i == space_indices[j]:
            reversed_string = reversed_string[:i] + ' ' + reversed_string[i:]
            j += 1
        if j >= len(space_indices):
            break
    
    return reversed_string