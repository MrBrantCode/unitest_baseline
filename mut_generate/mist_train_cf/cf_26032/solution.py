"""
QUESTION:
Create a function called pig_latin that takes a string of text as input and returns the string translated into Pig Latin. The function should split the input string into individual words, then for each word, move all consonants before the first vowel to the end of the word and append 'ay'. If the word begins with a vowel, simply append 'ay' to the end. The translated words should be joined back into a single string with spaces in between.
"""

def pig_latin(text):
    words = text.split()
    Latin_words = []
    for word in words:
        firstletter = word[0]
        if firstletter.lower() in 'aeiou':
            Latin_word = word+'ay'
        else:
            Latin_word = word[1:]+firstletter+'ay'
        Latin_words.append(Latin_word)
    return " ".join(Latin_words)