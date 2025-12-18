"""
QUESTION:
Write a function called `translate_and_reverse` that takes an English word as input, translates it into German, and then reverses each individual word in the translated text. For example, the word "Hello" translates to "Hallo" in German, and reversing each individual word would result in "ollaH".
"""

def translate_and_reverse(word):
    # Dictionary for word translation
    translations = {
        "hello": "hallo",
        # Add more translations as needed
    }
    
    # Convert the word to lowercase for translation lookup
    lower_word = word.lower()
    
    # Check if the word is in the translations dictionary
    if lower_word in translations:
        # Translate the word
        translated_word = translations[lower_word]
        
        # Reverse the translated word
        reversed_word = translated_word[::-1]
        
        # Return the reversed translated word
        return reversed_word
    else:
        # Return a message if the word is not found in the dictionary
        return "Word not found in dictionary"