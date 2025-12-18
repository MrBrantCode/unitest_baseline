"""
QUESTION:
An english word is given as input and it is modified using some format. Identify the format using the examples given below (examples given are sufficient to identify the format) and print the modified word as output.
STEWART is modified as EWARTSTAY, AMAR is modified as AMAR, MAN is modified as ANMAY etc.
Note: Input contains uppercase english words.
 
Example 1:
Input:
S = "GEEK"
Output:
EEKGAY
Explanation:
The string when modified gives "EEKGAY".
Example 2:
Input:
S = "ALL"
Output:
ALL
Explanation:
The string when modified remains the same.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function englishWords() which takes a String S as input and returns the modified String.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
 
Constraints:
1 <= |S| <= 10^{5}
"""

def modify_english_word(S: str) -> str:
    vowels = {'A', 'E', 'I', 'O', 'U'}
    prefix = ''
    suffix = ''
    
    for i, char in enumerate(S):
        if char not in vowels:
            prefix += char
        else:
            suffix = S[i:]
            break
    
    modified_word = suffix + prefix
    
    if modified_word == S:
        return S
    
    return modified_word + 'AY'