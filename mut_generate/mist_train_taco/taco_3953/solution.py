"""
QUESTION:
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
 









Example 1:
Input: "ab-cd"
Output: "dc-ba"


Example 2:
Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"


Example 3:
Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

 

Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S doesn't contain \ or "
"""

def reverse_only_letters(S: str) -> str:
    # Create a stack of all alphabetic characters in the string
    stack = [char for char in S if char.isalpha()]
    
    # Initialize an empty result string
    result = ''
    
    # Iterate through each character in the original string
    for char in S:
        # If the character is alphabetic, pop from the stack and append to result
        if char.isalpha():
            result += stack.pop()
        else:
            # If the character is not alphabetic, append it as is
            result += char
    
    return result