"""
QUESTION:
Create a function called `classify_words` that takes a list of strings as input and classifies them into two groups, 'positive' and 'negative', based on predefined lists of positive and negative words. The function should return a dictionary with 'positive' and 'negative' as keys and lists of corresponding words as values. Words that are not found in either list should be printed as unclassified. The function should be case-insensitive.
"""

positive_list = ["great", "good", "amazing", "nice", "love"]
negative_list = ["bad", "hate", "terrible", "ugly", "dislike"]

def classify_words(word_list):
    positive_words = []
    negative_words = []

    for word in word_list:
        if word.lower() in positive_list:
            positive_words.append(word)
        elif word.lower() in negative_list:
            negative_words.append(word)
        else:
            print(f"'{word}' is not classified, it could be neutral or not in the predefined list")

    return {'positive': positive_words, 'negative': negative_words}