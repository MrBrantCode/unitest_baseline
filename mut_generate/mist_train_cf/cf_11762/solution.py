"""
QUESTION:
Write a function named `detect_anagrams` that takes a list of words as input and returns a dictionary where the keys are the input words and the values are lists of their corresponding anagrams. The function should only include words that have at least one anagram in the output dictionary. The time complexity of the function should be O(n*mlogm), where n is the number of words and m is the average word length.
"""

def detect_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return {key: value for key, value in anagram_dict.items() if len(value) > 1}