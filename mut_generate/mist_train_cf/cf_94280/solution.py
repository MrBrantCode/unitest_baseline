"""
QUESTION:
Write a function `replace_last_occurrence(string, word)` that replaces the last occurrence of a given word in a string, making sure the replacement is case-insensitive and maintains the original capitalization of the word in the replaced string. The replacement should only happen if the last occurrence of the word is not part of another word.
"""

def replace_last_occurrence(string, word):
    # Split the string into a list of words
    words = string.split()
    
    # Iterate over the words in reverse order
    for i in range(len(words)-1, -1, -1):
        # Check if the current word matches the given word (ignoring case)
        if words[i].lower() == word.lower():
            # Check if it is the last occurrence (not part of another word)
            if i == len(words)-1 or not words[i+1].isalpha():
                # Replace the word while maintaining the original capitalization
                words[i] = words[i].replace(word, word, 1 if words[i].istitle() else -1)
                break
    
    # Join the list of words back into a string
    return ' '.join(words)