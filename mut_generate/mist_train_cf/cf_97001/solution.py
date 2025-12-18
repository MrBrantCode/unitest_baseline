"""
QUESTION:
Create a function named `convert_string_to_list` that takes a string as input and returns a list of words. The string consists of only lowercase alphabets and contains no punctuation marks. The function should exclude any words that start with a vowel, sort the remaining words in descending order based on their length, and have a time complexity of O(n log n), where n is the length of the input string.
"""

def convert_string_to_list(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    filtered_words = [word for word in words if not word[0] in vowels]
    sorted_words = sorted(filtered_words, key=lambda x: len(x), reverse=True)
    return sorted_words