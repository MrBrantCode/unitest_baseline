"""
QUESTION:
Create a function `encode_to_runes` that takes a string of English characters as input and returns a string where each character is replaced with its corresponding Elder Futhark rune symbol. The function should map the characters 'a' to 'ᚠ', 'b' to 'ᚢ', 'c' to 'ᚦ', 'd' to 'ᚩ', and 'e' to 'ᚱ', leaving other characters intact.
"""

def encode_to_runes(text):
    runes = {
        "a": "ᚠ",    # Rune represents wealth
        "b": "ᚢ",    # Rune represents aurochs, a form of wild cattle
        "c": "ᚦ",    # Rune represents thorn or a giant
        "d": "ᚩ",    # Rune refers to a god and a mouth
        "e": "ᚱ",    # Rune represents riding
    }
    encoded_text = ""
    for character in text:
        if character.lower() in runes:
            encoded_text += runes[character.lower()]
        else:
            encoded_text += character
    return encoded_text