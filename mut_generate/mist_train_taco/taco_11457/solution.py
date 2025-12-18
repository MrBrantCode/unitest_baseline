"""
QUESTION:
You are given an encoded string S of length N. The encoded string is mixed with some number of substring "LIE" and some secret message. You have to extract secret message from it by removing all the "LIE" substrings.
For example - "I AM COOL" is given as "LIEILIEAMLIELIECOOL".
Example 1:
Input: S = "LIEILIEAMLIELIECOOL"
Output: "I AM COOL"
Example 2:
Input: S = "LIELIEALIEBCLIE"
Output: "A BC"
Your Task:  
You don't need to read input or print anything. Your task is to complete the function ExtractMessage() which accepts a string as input parameter and returns a string containing secret message.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
String contains only Upper Case Letters.
"""

def extract_secret_message(s: str) -> str:
    # Split the string by "LIE"
    parts = s.split('LIE')
    
    # Filter out any empty strings that may result from the split
    filtered_parts = [part for part in parts if part]
    
    # Join the filtered parts with a space to form the secret message
    secret_message = ' '.join(filtered_parts)
    
    return secret_message