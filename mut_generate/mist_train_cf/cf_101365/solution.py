"""
QUESTION:
Write a function named `find_anagrams` that takes a list of words as input, and returns the unique words that can be formed by rearranging the letters of one or more of the words in the list. The function should handle duplicates, ignore case, and identify words that do not have any anagrams in the list.
"""

def find_anagrams(words):
    """
    This function takes a list of words as input, and returns the unique words that can be formed by rearranging 
    the letters of one or more of the words in the list. The function handles duplicates, ignores case, and 
    identifies words that do not have any anagrams in the list.

    Args:
        words (list): A list of words.

    Returns:
        list: A list of unique words that have anagrams in the input list.
    """
    anagrams = {}

    # iterate through the words
    for word in words:
        # sort the letters of the word and use it as a key
        key = ''.join(sorted(word.lower()))
        # if the key already exists, add the word to the list of anagrams
        if key in anagrams:
            anagrams[key].append(word)
        # otherwise, create a new key with the sorted string and add the word to the value list
        else:
            anagrams[key] = [word]

    # iterate through the dictionary and return the words that have more than one value
    result = []
    for key, value in anagrams.items():
        if len(value) > 1:
            result.extend(value)
    return list(set(result))