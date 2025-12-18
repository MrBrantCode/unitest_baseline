"""
QUESTION:
Write a function named word_freq_list that takes a string of text as input and returns a list of tuples, where each tuple contains a unique word from the text and its frequency of occurrence. The function should ignore case sensitivity, replace special characters and numbers with their ASCII values, and handle punctuation marks. The input string may contain a mix of words, special characters, and numbers.
"""

def word_freq_list(text):
    # Produces a word frequency list
    freq_dict = {}
    for el in text.split():
        # Checks if element contains only alphabets and ignore case sensitivity 
        if el.isalpha():  
            el = el.lower()
            # this will ensure the words are considered the same regardless of case 
            freq_dict[el] = freq_dict.get(el, 0) + 1
        else:
            # Checks if element contains special characters or numbers
            # Replaces them with their ASCII equivalent
            freq_dict.update({ord(c): text.count(str(c)) for c in el if not c.isalpha()})
    return [(k, v) for k, v in freq_dict.items()]