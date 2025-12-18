"""
QUESTION:
Write a function `shortest_substring` that takes two parameters: `words` (an array of strings) and `string` (a string that may contain special characters and spaces). The function should return the shortest word in the `words` array that is a substring of the `string`. If no such word exists, return `None`. The function should handle duplicate words in the `words` array.
"""

def shortest_substring(words, string):
    shortest_word = None
    shortest_length = float('inf')

    for word in words:
        if word in string and len(word) < shortest_length:
            shortest_word = word
            shortest_length = len(word)

    return shortest_word