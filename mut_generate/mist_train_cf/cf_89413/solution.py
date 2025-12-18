"""
QUESTION:
Write a function `find_shortest_subsequence` that takes a string and two words as input. The function should find the shortest subsequence containing both words and return it. If the words are not found in the string, return an error message. The function should handle cases where the words are not distinct and overlap in the string, as well as large input strings and special characters.
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
            length = max(word1_pos, word2_pos) + max(len(word1), len(word2)) - min(word1_pos, word2_pos)
            if length < min_length:
                min_length = length
                if word1_pos < word2_pos:
                    min_subsequence = string[word1_pos:word2_pos+len(word2)]
                else:
                    min_subsequence = string[word2_pos:word1_pos+len(word1)]
    
    if min_subsequence == "":
        return "Words not found in the string"
    
    return min_subsequence