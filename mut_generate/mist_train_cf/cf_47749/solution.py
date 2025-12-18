"""
QUESTION:
Write a function `lengthOfLongestSubstring(s)` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The function should be able to handle all possible ASCII characters.
"""

def lengthOfLongestSubstring(s):
    character_set = [0] * 128
    left = 0
    result = 0
    
    for right in range(len(s)):
        val = ord(s[right])
        if character_set[val] > 0:
            while character_set[val] > 0:
                character_set[ord(s[left])] -= 1
                left += 1
        character_set[val] += 1
        result = max(result, right - left + 1)
    
    return result