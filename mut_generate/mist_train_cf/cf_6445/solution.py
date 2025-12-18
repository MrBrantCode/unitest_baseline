"""
QUESTION:
Write a function `find_longest_word_without_e(string)` that finds the longest word in a given string that does not contain the letter 'e'. Implement this using recursion and achieve a time complexity of O(n), where n is the length of the string.
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