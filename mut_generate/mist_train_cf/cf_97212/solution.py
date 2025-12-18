"""
QUESTION:
Write a function `shortest_substring_word` that takes in two parameters: an array of words and a string. The function should find the shortest word in the array that is a substring of the string, ignoring case differences, and return it in lowercase. The words in the array and the characters in the string are case-sensitive during the search. The length of the words in the array and the string can be up to 100 characters.
"""

def shortest_substring_word(arr, string):
    shortest_word = "a" * 101
    for word in arr:
        if word.lower() in string.lower():
            if len(word) < len(shortest_word):
                shortest_word = word
    return shortest_word.lower()