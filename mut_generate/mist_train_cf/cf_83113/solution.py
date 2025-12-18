"""
QUESTION:
Write a function `kSimilarity(s1, s2)` that takes two anagram strings `s1` and `s2` as input and returns the smallest `k` for which `s1` and `s2` are `k`-similar, along with a list of all the swaps made to transform `s1` into `s2`. 

The function must consider that strings `s1` and `s2` are `k`-similar if we can swap the positions of two letters in `s1` exactly `k` times so that the resulting string equals `s2`.

Constraints: `1 <= len(s1) <= 100`, `len(s2) == len(s1)`, and `s1` and `s2` contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}. `s2` is an anagram of `s1`.
"""

def kSimilarity(s1, s2):
    swaps = []
    l_s1, l_s2 = list(s1), list(s2)
    
    for i in range(len(l_s1)):
        if l_s1[i] != l_s2[i]:
            for j in range(i + 1, len(l_s1)):
                if l_s1[j] == l_s2[i] and l_s1[j] != l_s2[j]:
                    l_s1[i], l_s1[j] = l_s1[j], l_s1[i]
                    swaps.append((i, j))
                    break
    return len(swaps), swaps