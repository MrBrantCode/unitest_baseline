"""
QUESTION:
Given a string of lowercase letters, write a function `rearrangeString` that rearranges the characters to form the lexicographically smallest string possible. The function should take in the string `name` and return the rearranged string. The rearranged string must not have leading zeroes, but since the input string only contains lowercase letters, this restriction is implicit.
"""

def rearrangeString(name: str) -> str:
    char_count = [0] * 26  
    for char in name:
        char_count[ord(char) - ord('a')] += 1  
    
    result = []  
    for i in range(26):
        while char_count[i] > 0:
            result.append(chr(i + ord('a')))  
            char_count[i] -= 1  
    
    return ''.join(result)  