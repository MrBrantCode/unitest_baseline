"""
QUESTION:
Create a function named `pig_latin` that takes a string sentence as input and returns the Pig Latin translation of the sentence. The function should convert each word in the sentence by moving the initial consonant or consonant cluster to the end of the word and adding "ay". If the word starts with a vowel, it should add "way" to the end. The function should handle any English sentence inputted by a user and return the translated sentence as a string.
"""

def pig_latin(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Create an empty list to store the Pig Latin words
    pig_latin_words = []
    # Loop through each word in the sentence
    for word in words:
        # If the word starts with a vowel, add "way" to the end
        if word[0] in "aeiou":
            pig_latin_words.append(word + "way")
        # If the word starts with a consonant, move the consonant(s) to the end and add "ay"
        else:
            pig_latin_words.append(word[1:] + word[0] + "ay")
    # Join the Pig Latin words back into a sentence
    pig_latin_sentence = " ".join(pig_latin_words)
    return pig_latin_sentence