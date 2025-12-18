"""
QUESTION:
Write a function `find_highest_similarity_pair(ss)` that takes a list of strings `ss` as input, compares each pair of strings in the list using the `SequenceMatcher` class, and returns the pair of strings with the highest similarity score as a tuple.

Input: `ss` is a list of strings where 2 <= len(ss) <= 100, and each string consists of lowercase letters and has a length between 1 and 100.
Output: A tuple of two strings representing the pair with the highest similarity score.
Restriction: If there are multiple pairs with the same highest similarity score, return the pair that appears first in the input list.
"""

from difflib import SequenceMatcher

def entrance(ss):
    max_similarity = 0
    max_pair = ()
    
    for i in range(len(ss)):
        x = ss[i]
        for j in range(i+1, len(ss)):
            y = ss[j]
            s = SequenceMatcher(None, x, y)
            similarity = s.ratio()
            if similarity > max_similarity:
                max_similarity = similarity
                max_pair = (x, y)
    
    return max_pair