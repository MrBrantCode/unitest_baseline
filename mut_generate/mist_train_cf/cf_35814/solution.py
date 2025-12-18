"""
QUESTION:
Write a function `is_anagram(s: str, t: str) -> bool` that determines whether string `t` is an anagram of string `s`, where an anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `True` if `t` is an anagram of `s`, and `False` otherwise. Assume that both strings only contain lowercase alphabets.
"""

def entrance(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_count = [0] * 26  # Assuming only lowercase alphabets
    t_count = [0] * 26  # Assuming only lowercase alphabets
    for char in s:
        s_count[ord(char) - ord('a')] += 1
    for char in t:
        t_count[ord(char) - ord('a')] += 1
    return s_count == t_count