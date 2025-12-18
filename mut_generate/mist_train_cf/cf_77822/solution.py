"""
QUESTION:
Create a function `find_max(words)` that takes a list of non-duplicated string inputs. The function should return the word with the highest number of distinct characters, ignoring case. If multiple words tie for the same unique character count, the function should return the earliest word in alphabetical order. The function must achieve a time complexity of O(n), where n is the number of words in the input list.
"""

def find_max(words):
    max_unique_count = 0
    max_unique_word = ""
    for word in words:
        unique_chars = len(set(word.lower()))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            max_unique_word = word
        elif unique_chars == max_unique_count:
            max_unique_word = min(max_unique_word, word)
    return max_unique_word