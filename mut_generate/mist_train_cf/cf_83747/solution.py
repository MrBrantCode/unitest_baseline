"""
QUESTION:
Write a function `shortest_subsequence(text, word1, word2)` that identifies the shortest subsequence in a given text that includes both `word1` and `word2` in order, but not directly bordering each other (i.e., with at least one word in between). Assume that `word1` and `word2` are present in the text and are case-sensitive. The function should handle punctuation by not considering it as part of the words. If multiple subsequences of the same length exist, return the leftmost one. If no valid subsequence is found, return "No valid sequence found."
"""

import string

def shortest_subsequence(text, word1, word2):
    tokens = text.split()
    min_len = len(tokens) + 1
    result = (0, 0)
    flag = False

    for i in range(len(tokens)):
        tokens[i] = tokens[i].strip(string.punctuation)
        if tokens[i] == word1:
            w1_index = i
            flag = True
        elif tokens[i] == word2 and flag:
            flag = False
            if (i - w1_index) < min_len and (i - w1_index) > 1:
                min_len = i - w1_index 
                result = (w1_index, i)
                
    if min_len == len(tokens) + 1:
        return "No valid sequence found."
    else:
        return " ".join(tokens[result[0]:result[1]+1])