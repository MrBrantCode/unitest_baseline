"""
QUESTION:
Write a function named `find_anagrams` that takes a list of strings and returns a dictionary where the keys are the input strings and the values are lists of anagrams for each string. The function should have a time complexity of O(n*mlogm), where n is the number of strings in the input list and m is the average length of the strings.
"""

def find_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        sorted_key = ''.join(sorted(string))
        if sorted_key in anagram_dict:
            anagram_dict[sorted_key].append(string)
        else:
            anagram_dict[sorted_key] = [string]
    return {key: value for key, value in anagram_dict.items() if len(value) > 1}