"""
QUESTION:
You are given a list of strings `A` and a string `B`. Define a function `numSpecialEquivGroups` that returns the number of groups of special-equivalent strings from `A`. Additionally, define another function `specialEquivalentStrings` that returns the group of special-equivalent strings from `A` that `B` can be made special equivalent to by making any number of moves.

A move onto `S` consists of swapping any two even indexed characters of `S`, or any two odd indexed characters of `S`. Two strings `S` and `T` are special-equivalent if after any number of moves onto `S`, `S == T`.

Restrictions:
`1 <= A.length <= 1000`
`1 <= A[i].length, B.length <= 20`
All `A[i]` and `B` have the same length.
All `A[i]` and `B` consist of only lowercase letters.
"""

import collections

def numSpecialEquivGroups(A):
    def normalize(S):
        return ''.join(sorted(S[0::2]) + sorted(S[1::2]))

    groups = set()
    for s in A:
        groups.add(normalize(s))
    return len(groups)