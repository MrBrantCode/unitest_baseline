"""
QUESTION:
Write a function `find_max` that takes a list of non-repeating strings as input and returns the string with the highest number of unique characters. The function should be case-insensitive, meaning it should disregard uppercase or lowercase differentiation. If multiple strings have the same number of unique characters, the function should return the string that comes first alphabetically. The function should have a time complexity of O(n), where n is the number of input strings.
"""

def find_max(words):
    def key_func(word):
        lower_word = word.lower()
        return (-len(set(lower_word)), lower_word)
      
    return min(words, key=key_func)