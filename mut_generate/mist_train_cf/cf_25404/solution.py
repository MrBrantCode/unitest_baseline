"""
QUESTION:
Create a function `translate_to_pig_latin` that translates a given sentence into Pig Latin. The translation rules are not explicitly stated, but based on the example, it appears that the function should move the first consonant (or consonant cluster) of each word to the end and append "ay".
"""

def translate_to_pig_latin(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    translated_words = []
    
    for word in words:
        if word[0].lower() in vowels:
            translated_words.append(word + 'way')
        else:
            vowel_index = 0
            for char in word:
                if char.lower() in vowels:
                    break
                vowel_index += 1
            translated_words.append(word[vowel_index:] + word[:vowel_index] + 'ay')
    
    return ' '.join(translated_words)