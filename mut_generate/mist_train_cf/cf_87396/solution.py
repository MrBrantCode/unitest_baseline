"""
QUESTION:
Create a function named `capitalize_words` that capitalizes the first letter of each word in a given string. The function should handle multiple whitespace characters between words, ignore leading and trailing whitespace, and only capitalize the first alphabetic character of each word. The input string can contain punctuation, special characters, and both lowercase and uppercase letters. The function should return the modified string with the capitalized first letters.
"""

def capitalize_words(string):
    string = string.strip()
    words = string.split()
    for i in range(len(words)):
        word = words[i]
        if word[0].isalpha():
            words[i] = word[0].upper() + word[1:]
    return ' '.join(words)