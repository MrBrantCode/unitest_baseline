"""
QUESTION:
Write a function named `pig_latin` that takes an English sentence as input and returns the corresponding Pig Latin sentence. The Pig Latin sentence should be created by moving the initial consonant or consonant cluster of each word to the end of the word, followed by "ay". If a word starts with a vowel, "way" should be added to the end. The function should be able to handle any English sentence input.
"""

def pig_latin(sentence):
    words = sentence.split()
    pig_latin_words = []
    for word in words:
        if word[0].lower() in "aeiou":
            pig_latin_words.append(word + "way")
        else:
            vowel_index = 0
            for char in word:
                if char.lower() in "aeiou":
                    break
                vowel_index += 1
            pig_latin_words.append(word[vowel_index:] + word[:vowel_index] + "ay")
    pig_latin_sentence = " ".join(pig_latin_words)
    return pig_latin_sentence