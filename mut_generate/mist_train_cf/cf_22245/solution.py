"""
QUESTION:
Write a function `convert_string_to_list` that takes a string of lowercase alphabets as input and returns a list of words in descending order of their lengths, excluding words that start with a vowel. The input string will not contain any punctuation marks and the time complexity of the solution should be O(n log n), where n is the length of the input string.
"""

def convert_string_to_list(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    filtered_words = [word for word in words if word[0] not in vowels]
    sorted_words = sorted(filtered_words, key=len, reverse=True)
    return sorted_words