"""
QUESTION:
Create a function called `unique_subsets` that takes a list `s` as input and returns a list of all unique subsets of `s`, preserving the original order of elements. The input list can contain duplicates, which should be treated as distinct elements in the subsets. The function should be able to handle lists of numbers and strings.
"""

def unique_subsets(s):
   return [ [s[j] for j in range(len(s)) if (i & 1 << j)] for i in range(1 << len(s)) ]