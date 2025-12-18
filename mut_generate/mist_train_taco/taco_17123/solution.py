"""
QUESTION:
Given a string S that consists of only alphanumeric characters and dashes. The string is separated into N + 1 groups by N dashes. Also given an integer K. 
We want to reformat the string S, such that each group contains exactly K characters, except for the first group, which could be shorter than K but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
Return the reformatted string.
Example 1:
Input: 
S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two
parts, each part has 4 characters. Note that two
extra dashes are not needed and can be removed.
Example 2:
Input:
S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string s has been split 
into three parts, each part has 2 characters 
except the first part as it could
be shorter as mentioned above.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function ReFormatString() which takes a string S and an integer K as input and returns the reformatted string.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ S.length() ≤ 10^{5}
1 ≤ K ≤ 10^{4}
"""

def reformat_string(S: str, K: int) -> str:
    # Remove all dashes and convert to uppercase
    cleaned_string = ''.join(char.upper() for char in S if char != '-')
    
    # Initialize the result list
    result = []
    
    # Calculate the length of the first group
    first_group_length = len(cleaned_string) % K
    if first_group_length == 0:
        first_group_length = K
    
    # Add the first group to the result
    result.append(cleaned_string[:first_group_length])
    
    # Add the remaining groups to the result
    for i in range(first_group_length, len(cleaned_string), K):
        result.append(cleaned_string[i:i + K])
    
    # Join the groups with dashes and return the result
    return '-'.join(result)