"""
QUESTION:
Write a function `capitalize_chars` that takes two parameters: `text` (the input string) and `n` (the number of characters to be capitalized from the start of each word). The function should capitalize the first `n` characters of each word in the input string and return the resultant string. If any word in the string has fewer characters than `n`, the function should return an error message indicating the word with insufficient characters.
"""

def capitalize_chars(text, n):
    words = text.split()
    new_words = []
    
    for word in words:
        if len(word) < n:
            return "Error: The word '{}' has characters less than specified number!".format(word)

        new_word = word[:n].upper() + word[n:]
        new_words.append(new_word)

    return ' '.join(new_words)