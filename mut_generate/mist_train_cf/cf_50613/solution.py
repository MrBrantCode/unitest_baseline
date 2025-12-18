"""
QUESTION:
Write a Python function called `word_tally` that takes a string `text` as input and returns a dictionary where the keys are the unique words in the text and the values are their respective counts. The function should ignore case when counting words and exclude common stop words like 'a', 'the', 'in', etc. The input string may contain multiple spaces between words and the words may be in any case.
"""

def word_tally(text):
    # List of common stop words
    stop_words = ['a', 'an', 'the', 'in', 'on', 'of', 'with', 'and', 'is', 'it', 'to']

    word_list = text.split() # split the text into words
    word_dict = {}
    for word in word_list:
        word = word.lower() # convert to lowercase to handle case-insensitive comparison
        if word not in stop_words: 
            if word in word_dict:
                word_dict[word] += 1 # increase the count if the word is already in the dictionary
            else:
                word_dict[word] = 1 # add the word to the dictionary if it's not already there
    return word_dict