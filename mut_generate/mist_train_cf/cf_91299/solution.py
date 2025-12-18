"""
QUESTION:
Create a function `classify_sentence` that takes a sentence as input and returns a string indicating whether the sentence is "Short", "Medium", or "Long" based on the number of words it contains. A sentence is considered short if it has less than 5 words, medium if it has between 5 and 10 words, and long if it has more than 10 words.
"""

def classify_sentence(sentence):
    words = sentence.split()
    num_words = len(words)
    
    if num_words < 5:
        return "Short"
    elif num_words >= 5 and num_words <= 10:
        return "Medium"
    else:
        return "Long"