"""
QUESTION:
Create a function named `find_al_words` that takes a string of text as input and returns a list of words containing the substring "al". The function should work for a text document of size n and m words, with each word having a maximum length of k. Implement the function with a time complexity of O(n + mk), where n is the size of the document, m is the number of words, and k is the maximum length of a word.
"""

def find_al_words(text):
    words = text.split()
    al_words = [word for word in words if 'al' in word]
    return al_words