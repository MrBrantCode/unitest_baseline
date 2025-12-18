"""
QUESTION:
Create a function `extract_extreme_emotion_words(text)` that takes a string of text as input and returns a list of extreme emotion words found in the text. Extreme emotion words include words such as 'great', 'awesome', 'amazing', 'interesting', 'intriguing', 'excellent', 'fantastic', 'exceptional', 'perfect', and 'wonderful'. The function should ignore non-extreme emotion words and perform a case-insensitive match.
"""

def extract_extreme_emotion_words(text):
    # your list of extreme emotion words
    extreme_emotion_words = ['great', 'awesome', 'amazing', 'interesting', 'intriguing',
                             'excellent', 'fantastic', 'exceptional', 'perfect', 'wonderful']

    # split the text into a list of words and check if each word is in the list of extreme emotion words
    return [word for word in text.split() if word.lower() in extreme_emotion_words]