"""
QUESTION:
Create a function called `capitalize_words` that takes a string as input and returns the modified string. The function should capitalize the first letter of each word in the string, ignoring leading and trailing whitespace, multiple whitespace characters between words, and non-alphabetic characters. The function should handle both lowercase and uppercase letters, words that contain numbers or special characters, and words that start with a special character or a number.
"""

def capitalize_words(string):
    string = string.strip()
    words = string.split()
    for i in range(len(words)):
        word = words[i]
        if word[0].isalpha():
            words[i] = word[0].upper() + word[1:]
    capitalized_string = ' '.join(words)
    return capitalized_string