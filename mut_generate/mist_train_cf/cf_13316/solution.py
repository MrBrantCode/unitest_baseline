"""
QUESTION:
Write a function named `find_shortest_subsequence` that takes a string and two words as input and returns the shortest subsequence containing both words. The subsequence must appear in the same order as they do in the original string, but not necessarily consecutively. The function should return any subsequence if multiple subsequences have the same minimum length. It is assumed that the two words are distinct and exist in the string.
"""

def find_shortest_subsequence(string, word1, word2):
    word1_pos = -1
    word2_pos = -1
    min_length = float('inf')
    for i in range(len(string)):
        if string[i:i+len(word1)] == word1:
            word1_pos = i
        if string[i:i+len(word2)] == word2:
            word2_pos = i
        if word1_pos != -1 and word2_pos != -1:
            subsequence_length = max(word1_pos, word2_pos) - min(word1_pos, word2_pos) + len(word2)
            if subsequence_length < min_length:
                min_length = subsequence_length
    return string[min(word1_pos, word2_pos):max(word1_pos, word2_pos) + len(word2)]