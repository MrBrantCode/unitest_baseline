"""
QUESTION:
Write a function `find_words_with_substring` that takes a string `document` as input and returns a list of words that contain the substring "al". The function should not use any built-in string matching or substring searching functions. The size of the document is n and the number of words in the document is m.
"""

def find_words_with_substring(document):
    words = document.split()
    words_with_substring = []

    for word in words:
        for i in range(len(word) - 1):
            if word[i] == 'a' and word[i+1] == 'l':
                words_with_substring.append(word)
                break

    return words_with_substring