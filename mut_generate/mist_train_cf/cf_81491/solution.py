"""
QUESTION:
Create a function `isAnagram(s: str, t: str) -> (bool, dict)` that takes two strings `s` and `t` as input. The function should return a tuple containing a boolean indicating whether `t` is an anagram of any permutation of `s`, and a dictionary containing the frequency count of each character in the anagram if it exists, otherwise an empty dictionary. The function should assume that `1 <= s.length, t.length <= 5000` and `s` and `t` consist of only lowercase English letters.
"""

from collections import Counter

def isAnagram(s: str, t: str) -> (bool, dict):
    s_counter, t_counter = Counter(s), Counter(t)
    if s_counter == t_counter:
        return True, dict(s_counter)
    else:
        return False, {}