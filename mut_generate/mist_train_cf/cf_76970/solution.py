"""
QUESTION:
Separate a given string into its constituent words using a single space for delineation. The input string does not contain spaces, and the function should use a dictionary of valid words to identify the word boundaries. Implement a function `separate_string(txt, dictionary)` that takes the input string `txt` and the dictionary of valid words as parameters and returns the string with spaces separating the constituent words.
"""

def separate_string(txt, dictionary):
    start = 0
    words = []
    while start < len(txt):
        for i in range(len(txt), start, -1):
            substr = txt[start:i]
            if substr in dictionary:
                words.append(substr)
                start = i
                break
    return ' '.join(words)