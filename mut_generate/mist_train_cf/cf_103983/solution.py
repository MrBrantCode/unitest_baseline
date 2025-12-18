"""
QUESTION:
Design a function 'sortString' that takes a string of words as input and returns the string with each word sorted alphabetically. Each word must consist only of lowercase letters and have a maximum length of 10 characters. The output string should maintain the original word order. The input string may contain up to 100 words separated by spaces.
"""

def sortString(s):
    words = s.split()  # Split the input string into a list of words
    sorted_words = ["".join(sorted(word)) for word in words]  # Sort each word alphabetically
    return " ".join(sorted_words)  # Join the sorted words back into a string with spaces between them