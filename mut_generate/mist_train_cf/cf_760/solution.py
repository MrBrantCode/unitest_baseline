"""
QUESTION:
Create a function `word_lengths` that takes a list of words as input and returns a dictionary where the keys are the words and the values are the lengths of the words. The input list will only contain lowercase letters and words with lengths between 1 and 20 characters. The function should handle cases where the input list is empty or contains duplicate words by only adding the first occurrence of each word to the dictionary. Do not use dictionary comprehension or built-in Python functions for this task.
"""

def word_lengths(words):
    def helper(words, dictionary):
        if not words:
            return dictionary
        word = words[0]
        if word not in dictionary:
            dictionary[word] = len(word)
        return helper(words[1:], dictionary)

    return helper(words, {})