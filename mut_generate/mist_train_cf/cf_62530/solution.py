"""
QUESTION:
Given a list `strs` of strings where every string in `strs` is an anagram of every other string in `strs`, write a function `num_similar_group` that returns a tuple of two values: the number of groups of similar strings and the size of the largest group. A string `X` is similar to string `Y` if we can swap two letters (in different positions) of `X` so that it equals `Y`, or if they are equal. The input constraints are: `1 <= strs.length <= 1000` and `1 <= strs[i].length <= 1000`, and `strs[i]` consists of lowercase letters only.
"""

def num_similar_group(strs):
    from collections import defaultdict
    anagram_dict = defaultdict(list)

    for s in strs:
        anagram_dict[''.join(sorted(s))].append(s)

    return len(anagram_dict), max(len(v) for v in anagram_dict.values())