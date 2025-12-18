"""
QUESTION:
Write a function `words_string(s, target)` that takes a string `s` of words separated by commas, spaces, or a combination of both and a target word `target`. Return an array of the words in their original order with all occurrences of the target word removed, the remaining words reversed, and sorted in alphabetical order.
"""

def words_string(s, target):
    words = s.replace(',', '').split()
    words = [word for word in words if word != target]
    words = [word[::-1] for word in words]
    words.sort()
    return words