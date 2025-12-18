"""
QUESTION:
Implement the `convert_to_title_case` function that converts a given string to title case without using Python's built-in `title()` function. The function should capitalize the first letter of each word unless it is a preposition, in which case it should be in lowercase. Prepositions include words like "on", "in", "at", "over", "beneath", "under", "for", "with", and "of". The function should also preserve any punctuation marks and their original positions in the string.
"""

def convert_to_title_case(input_str):
    prepositions = ["on", "in", "at", "over", "beneath", "under", "for", "with", "of", "a"]
    words = input_str.split()
    title_case_words = []
    
    for word in words:
        # strip punctuations from the word for comparisons
        clean_word = ''.join(e for e in word if e.isalnum())
        if clean_word.lower() in prepositions:
            title_case_words.append(word.lower())
        else:
            title_case_words.append(word.capitalize())
    
    # join the words using ' ' as separator and return the output
    return ' '.join(title_case_words)