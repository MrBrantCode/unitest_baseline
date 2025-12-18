"""
QUESTION:
Implement a function `search_word(string, word)` that searches for a given word within a string without using built-in string search or matching functions. The function should return the starting position of the word if found, and -1 if not found. The algorithm must meet the following requirements: 
- Time complexity: O(n), where n is the length of the string
- Space complexity: O(1), with no additional data structures used to store intermediate results.
"""

def search_word(string, word):
    string_len = len(string)
    word_len = len(word)

    for i in range(string_len - word_len + 1):
        match = True
        for j in range(word_len):
            if string[i + j] != word[j]:
                match = False
                break
        if match:
            return i

    return -1