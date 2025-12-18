"""
QUESTION:
Write a function named `find_shortest_subsequence` that takes a string and two distinct words as input, and returns the shortest subsequence containing both words. The function should return any subsequence in case of a tie. The words are guaranteed to exist in the string.
"""

def find_shortest_subsequence(string, word1, word2):
    # Initialize word pointers
    word1_pos = -1
    word2_pos = -1
    # Initialize minimum subsequence length
    min_length = float('inf')
    # Initialize minimum subsequence
    min_subsequence = ""
    # Iterate through the string character by character
    for i in range(len(string)):
        # If the current character matches word1, update word1 position
        if string[i:i+len(word1)] == word1:
            word1_pos = i
        # If the current character matches word2, update word2 position
        if string[i:i+len(word2)] == word2:
            word2_pos = i
        # If both word pointers have been updated, calculate subsequence length
        if word1_pos != -1 and word2_pos != -1:
            subsequence_length = max(word1_pos, word2_pos) - min(word1_pos, word2_pos) + len(word2)
            # Update minimum subsequence length if necessary
            if subsequence_length < min_length:
                min_length = subsequence_length
                min_subsequence = string[min(word1_pos, word2_pos):max(word1_pos, word2_pos) + len(word2)]
    # Return the shortest subsequence found
    return min_subsequence