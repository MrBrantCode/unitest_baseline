"""
QUESTION:
Given a string, eliminate all “b” and “ac” in the string, replace them in-place and iterate over the string once.
Example 1:
Input: str = "aacbacc"
Output: ac
Explanation: Iterate once and remove
occurrence of "b" and "ac"
Example 2:
Input: str = "aacb"
Output: a
Explanation: Iterate once and remove
occurrence of "b" and "ac"
Your task:
Your task is to complete the function stringFilter() which takes a single string as input and modify the string as mentioned above. You need not take any input or print anything.
 
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)
Constraints:
1 <= |S| <= 10^{5}
String contains lower case alphabets
"""

def string_filter(input_str: str) -> str:
    # Initialize an empty list to store the filtered characters
    filtered_chars = []
    
    # Initialize an index to keep track of the current character
    i = 0
    
    # Iterate over the string once
    while i < len(input_str):
        # If the current character is 'b', skip it
        if input_str[i] == 'b':
            i += 1
        # If the current character is 'a' and the next character is 'c', skip both
        elif i < len(input_str) - 1 and input_str[i] == 'a' and input_str[i + 1] == 'c':
            i += 2
        # Otherwise, add the current character to the filtered list
        else:
            filtered_chars.append(input_str[i])
            i += 1
    
    # Join the filtered characters into a string and return it
    return ''.join(filtered_chars)