"""
QUESTION:
Construct a function `min_substring(s)` that takes an input string `s` and returns the minimal length substring that contains all unique alphabets present in the string. The function should consider only alphabets and ignore any duplicate characters in the substring.
"""

def min_substring(s):
    char_set = set()
    char_dict = {}
    left = 0
    min_length = float('inf')
    min_sub_str = ""
    
    for right in range(len(s)):
        if s[right] not in char_dict:
            char_set.add(s[right])
        char_dict[s[right]] = char_dict.get(s[right], 0) + 1

        while len(char_set) == len(char_dict) and left <= right:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_sub_str = s[left:right+1]
            
            if char_dict[s[left]] == 1:
                char_dict.pop(s[left])
            else:
                char_dict[s[left]] -= 1
            left += 1

    return min_sub_str