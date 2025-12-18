"""
QUESTION:
Write a Python function named `translate_to_emoji` that takes a string `text` as input and returns a string where certain words are translated to their corresponding emojis based on a predefined dictionary. The function should split the input string into individual words, replace each word with its corresponding emoji if available in the dictionary, and join the translated words back into a string.

The dictionary `emoji_dict` that maps words to emojis should be predefined. The function should return the original word if it does not have a corresponding emoji in the dictionary.
"""

emoji_dict = {
    "happy": "😊",
    "sad": "😞",
    "laughing": "😂",
    # Add more mappings.
}

def translate_to_emoji(text):
    words = text.split()
    translated_words = [emoji_dict.get(word, word) for word in words]
    return " ".join(translated_words)