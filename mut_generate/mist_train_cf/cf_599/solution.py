"""
QUESTION:
Write a function `find_anagrams` that takes a list of strings as input. The function should return a list of strings, where each string is a representative of a set of anagrams from the input list. The function should ignore case sensitivity and have a time complexity of O(n*m*log(m)), where n is the length of the input list and m is the average length of the strings in the list.
"""

def find_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]
    
    result = []
    for key in anagrams:
        if len(anagrams[key]) > 1:
            result.append(anagrams[key][0])
    
    return result