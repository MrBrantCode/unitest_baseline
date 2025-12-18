"""
QUESTION:
Replace all occurrences of 'a' or 'A' in a string with an underscore symbol, preserving the original case, but only if the 'a' or 'A' is immediately preceded and followed by a vowel. The vowels are 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'. Return the modified string.
"""

def modify_string(s):
    vowels = set('aeiouAEIOU')
    result = ''
    for i, char in enumerate(s):
        if char.lower() == 'a' and (i > 0 and s[i-1] in vowels and i < len(s)-1 and s[i+1] in vowels):
            result += '_' if char.islower() else '_'
        else:
            result += char
    return result