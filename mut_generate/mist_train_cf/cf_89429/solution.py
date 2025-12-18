"""
QUESTION:
Implement a recursive function named `find_longest_word_without_e` that takes a string as input and returns the longest word without the letter 'e'. The function must have a time complexity of O(n), where n is the length of the input string.
"""

def find_longest_word_without_e(string):
    def find_longest_word(words, longest_word):
        if not words:
            return longest_word
        word = words.pop(0)
        if 'e' not in word:
            if len(word) > len(longest_word):
                longest_word = word
        return find_longest_word(words, longest_word)
    
    words = string.split()
    longest_word = find_longest_word(words, "")
    return longest_word