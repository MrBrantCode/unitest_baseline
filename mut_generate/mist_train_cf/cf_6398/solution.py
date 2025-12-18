"""
QUESTION:
Write a function `find_shortest_subsequence(string, word1, word2)` that finds the shortest subsequence containing both `word1` and `word2` in the given `string`. The function should return the lexicographically smallest subsequence found among all subsequences with the minimum length. If `word1` and `word2` are not present in the string, return "Words not found in the string".
"""

def find_shortest_subsequence(string, word1, word2):
    word1_pos = -1
    word2_pos = -1
    min_length = float('inf')
    min_subsequence = ""
    
    for i in range(len(string)):
        if string[i:].startswith(word1):
            word1_pos = i
        if string[i:].startswith(word2):
            word2_pos = i
            
        if word1_pos != -1 and word2_pos != -1:
            start = min(word1_pos, word2_pos)
            end = max(word1_pos + len(word1) - 1, word2_pos + len(word2) - 1)
            length = end - start + 1
            if length < min_length:
                min_length = length
                min_subsequence = string[start:end + 1]
    
    if min_subsequence == "":
        return "Words not found in the string"
    
    return min_subsequence