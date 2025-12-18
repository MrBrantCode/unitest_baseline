"""
QUESTION:
Write a function `enhancedTotalMatch(lst1, lst2)` that takes two lists of strings `lst1` and `lst2` as input. The function should return a list containing two elements: the list with fewer total characters, and a list of anagram-pairs found in `lst1` and `lst2`. If both lists have the same total number of characters, return the first list. The comparison should be case-insensitive.
"""

def enhancedTotalMatch(lst1, lst2):
    anagrams = [[w1, w2] for w1 in lst1 for w2 in lst2 if sorted(w1.lower()) == sorted(w2.lower())]
    count1, count2 = sum(len(w) for w in lst1), sum(len(w) for w in lst2)
    if count1 <= count2:
        return [lst1, anagrams]
    else:
        return [lst2, anagrams]