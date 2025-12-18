"""
QUESTION:
Create a function `largestMerge(word1: str, word2: str) -> str` that constructs the lexicographically largest string `merge` by choosing characters from two input strings `word1` and `word2`. The function should follow these rules: 
1. While either `word1` or `word2` are non-empty, choose one of the following options: 
   - If `word1` is non-empty, append the first character in `word1` to `merge` and delete it from `word1`.
   - If `word2` is non-empty, append the first character in `word2` to `merge` and delete it from `word2`.
2. Return the lexicographically largest `merge` that can be constructed.

Additionally, implement a function `countVowels(merge: str) -> int` that counts the number of vowels in the `merge` string.

Constraints: 
- `1 <= word1.length, word2.length <= 5000`
- `word1` and `word2` consist only of lowercase English letters.
"""

def largestMerge(word1: str, word2: str) -> str:
    if not word1:
        return word2
    elif not word2:
        return word1
    if word1>word2:
        return word1[0] + largestMerge(word1[1:], word2)
    else:
        return word2[0] + largestMerge(word1, word2[1:])

def countVowels(merge: str) -> int:
    count = 0
    for character in merge:
        if character in 'aeiou':
            count += 1
    return count