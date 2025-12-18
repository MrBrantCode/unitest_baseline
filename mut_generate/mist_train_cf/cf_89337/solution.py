"""
QUESTION:
Create a function named `replace_with_numbers(text)` that takes a string of text as input and returns a comma-separated string of numbers. Each number is calculated by summing the ASCII values of the letters in the word, then dividing the sum by the position of the letter in the alphabet. If the resulting number is odd, add 1 to it. If the resulting number is even, subtract 1 from it. Ignore any non-alphabetic characters in the text. The input text will not contain any duplicate letters and will contain up to 5 non-alphabetic characters.
"""

def replace_with_numbers(text):
    numbers = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in text:
        ascii_value = ord(letter.lower())
        if letter.isalpha():
            position = alphabet.index(letter.lower()) + 1
            total = sum(ord(char.lower()) for char in letter) // position
            if total % 2 == 0:
                total -= 1
            else:
                total += 1
            numbers.append(str(total))
    return ','.join(numbers)