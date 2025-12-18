"""
QUESTION:
Write a function `maxRepeating(sequence: str, word: str) -> int` that returns the maximum `k`-repeating value of `word` in `sequence`, where `k` is the highest value where `word` concatenated `k` times is a substring of `sequence`. If `word` is not a substring of `sequence`, return `0`. The input strings `sequence` and `word` contain only lowercase English letters, and their lengths are between 1 and 1000, inclusive.
"""

def maxRepeating(sequence: str, word: str) -> int:
    len_sequence, len_word = len(sequence), len(word)
    max_count = 0
    for i in range(len_sequence):
        j = i
        count = 0
        while sequence[j:j+len_word] == word:
            j += len_word
            count += 1
        max_count = max(count, max_count)
    return max_count