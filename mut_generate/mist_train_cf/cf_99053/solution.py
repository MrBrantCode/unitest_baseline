"""
QUESTION:
Write a function called `find_anagrams` that takes a list of words as input and returns a dictionary where the keys are the sorted letters of the words and the values are lists of words that can be formed by rearranging those letters. The function should handle duplicates and ignore case.
"""

def find_anagrams(words):
    anagrams = {}
    
    for word in words:
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    
    return {key: value for key, value in anagrams.items() if len(value) > 1}