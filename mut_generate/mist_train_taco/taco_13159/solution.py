"""
QUESTION:
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:


Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:


Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:


Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:


Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

def follows_pattern(pattern: str, str: str) -> bool:
    str_arr = str.split()
    pattern_dict = {}
    str_dict = {}
    pattern_tokenize = []
    token_p = 0
    str_tokenize = []
    token_s = 0
    
    for char in pattern:
        if char not in pattern_dict:
            pattern_dict[char] = token_p
            token_p += 1
        pattern_tokenize.append(pattern_dict[char])
    
    for word in str_arr:
        if word not in str_dict:
            str_dict[word] = token_s
            token_s += 1
        str_tokenize.append(str_dict[word])
    
    return pattern_tokenize == str_tokenize