"""
QUESTION:
Create a function called `morse_converter` that takes a sentence as input and returns its Morse code sequence. The function should use a dictionary to map English letters to Morse code and handle non-alphabetic characters by inserting a space in their place. Spaces between words in the sentence should be denoted by a slash ("/") in the Morse code. The output Morse code sequence should have a space between each Morse code letter.
"""

def morse_converter(sentence):
    morse_code = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.",
            "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..",
            "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.",
            "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-",
            "Y" : "-.--", "Z" : "--..", " " : "/"}

    sentence = sentence.upper()
    morse = ''

    for char in sentence:
        if char not in morse_code:
            morse += ' '
        else:
            morse += morse_code[char] + ' '

    return morse