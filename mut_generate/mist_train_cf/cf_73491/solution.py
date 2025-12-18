"""
QUESTION:
Write a function called `maxMerge` that takes two strings `word1` and `word2` as input, each consisting solely of lowercase English alphabets with lengths between 1 and 3000. The function should return the lexicographically maximum string that can be created by concatenating characters from `word1` and `word2`, with the constraint that characters from each string must be used in the order they appear.
"""

def maxMerge(word1, word2):
    i = j = 0
    merge = ""

    while i < len(word1) or j < len(word2):
        if word1[i:] > word2[j:]:
            merge += word1[i]
            i += 1
        else:
            merge += word2[j]
            j += 1

    return merge