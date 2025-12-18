"""
QUESTION:
Write a function called `translate_and_exclude` that takes an English sentence as input and returns its Spanish translation, excluding any words that contain the letter "e".
"""

def translate_and_exclude(sentence):
    # Define a dictionary for English to Spanish translation
    translation_dict = {
        'the': 'el',
        'fox': 'zorro',
        'brown': 'marrón',
        'jumps': 'salta',
        'over': 'sobre',
        'lazy': 'perezoso',
        'dog': 'perro'
    }
    
    # Split the input sentence into words
    words = sentence.split()
    
    # Initialize an empty list to store translated words
    translated_words = []
    
    # Iterate over each word in the input sentence
    for word in words:
        # Check if the word contains the letter "e" (ignoring case)
        if 'e' not in word.lower():
            # If the word does not contain "e", translate it and add to the list
            translated_words.append(translation_dict.get(word.lower(), word))
    
    # Join the translated words back into a sentence
    translated_sentence = ' '.join(translated_words)
    
    return translated_sentence