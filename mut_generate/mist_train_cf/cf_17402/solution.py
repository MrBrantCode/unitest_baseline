"""
QUESTION:
Write a function named `replace_whitespace` that takes a string as input and replaces all occurrences of the word "whitespace" with the character '*'. The function should be case-sensitive, treat "whitespace" as a whole word or as a substring of another word, and handle multiple occurrences of "whitespace" in the string. The input string will not be empty and will not contain any leading or trailing spaces.
"""

def replace_whitespace(string):
    # Split the string into words
    words = string.split()
    # Initialize an empty list to store the modified words
    modified_words = []
    # Iterate through each word in the list
    for word in words:
        # Check if the word is exactly equal to "whitespace"
        if word == "whitespace":
            # If it is, replace it with "*"
            modified_words.append("*")
        # Check if the word contains "whitespace" as a substring
        elif "whitespace" in word:
            # If it does, replace all occurrences of "whitespace" with "*"
            modified_word = word.replace("whitespace", "*")
            modified_words.append(modified_word)
        # If the word does not need to be modified, add it to the list as is
        else:
            modified_words.append(word)
    # Join the modified words into a string with spaces in between
    modified_string = " ".join(modified_words)
    return modified_string