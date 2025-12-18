"""
QUESTION:
You have given a non-empty string. This string can consist of lowercase and uppercase english alphabets. Convert the string into an alternating sequence of lowercase and uppercase characters without changing the character at the 0th index.
Example 1:
Input:
S = "geeksforgeeks"
Output: gEeKsFoRgEeKs
Explanation: The first character is kept
unchanged whereas all the characters are
arranged in alternating order of lowercase
and uppercase.
Ã¢â¬â¹Example 2:
Input: 
S = "Geeksforgeeks"
Output: GeEkSfOrGeEkS
Explanation: The first character is kept
unchanged whereas all the characters are
arranged in alternating order of lowercase
and uppercase.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getCrazy() which takes the string S as input and returns the resultant string by making the stated modifications.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def convert_to_alternating_case(S: str) -> str:
    if not S:
        return S
    
    # Determine the initial case of the first character
    if S[0].islower():
        flag = True
    else:
        flag = False
    
    # Initialize the result string
    result = ''
    
    # Iterate through the string and build the result
    for char in S:
        if flag:
            result += char.lower()
        else:
            result += char.upper()
        flag = not flag
    
    return result