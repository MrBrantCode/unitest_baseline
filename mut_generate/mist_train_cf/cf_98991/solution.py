"""
QUESTION:
Create a function `pig_latin(sentence)` that takes an English sentence as input and returns its Pig Latin translation. The function should handle any English sentence and move the initial consonant or consonant cluster of each word to the end, followed by "ay". If a word starts with a vowel, add "way" to the end. The resulting Pig Latin sentence should be a string with the same grammatical correctness and meaning as the original English sentence.
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