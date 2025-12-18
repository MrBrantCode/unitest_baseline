"""
QUESTION:
Write a function called `is_anagram` that takes a string and a list of words as input and returns True if the string is an anagram of any word in the list, False otherwise. The function should be case-insensitive, ignore special characters and spaces, and handle words in the list that are longer than the input string.
"""

def is_anagram(s, word_list):
    s = ''.join(e for e in s.lower() if e.isalnum())
    for word in word_list:
        word = ''.join(e for e in word.lower() if e.isalnum())
        if len(s) != len(word):
            continue
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1
        word_freq = {}
        for char in word:
            word_freq[char] = word_freq.get(char, 0) + 1
        if s_freq == word_freq:
            return True
    return False