"""
QUESTION:
Write a function named `word_frequency` that takes a string `text` and a list of words `words` as input. The function should return a dictionary where the keys are the individual words from the list and the values are their respective frequency of appearances in the text, ignoring case and punctuation.
"""

def word_frequency(text, words):
    # replace punctuation with whitespaces
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for x in text.lower(): 
        if x in punctuations: 
            text = text.replace(x, " ")
            
    # split the text into list of words
    split_text = text.lower().split()
    
    # create a dictionary with word frequencies
    frequency_dict = {word: split_text.count(word) for word in words}
    
    return frequency_dict