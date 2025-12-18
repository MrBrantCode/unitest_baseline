"""
QUESTION:
Create a function called `caesar_encrypt` that takes in two parameters: `text` and `shift`. The function should perform a Caesar Cipher encryption on the input `text` by shifting each alphabetic character by the specified `shift` value, while leaving non-alphabetic characters unchanged. The function should handle both uppercase and lowercase letters, and it should efficiently wrap around the alphabet if the shift value exceeds 26.
"""

def caesar_encrypt(text, shift):
  result = ''

  # traverse text
  for i in range(len(text)):
    char = text[i]

    # Encrypt uppercase characters
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)

    # Encrypt lowercase characters
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)

    # Leave other characters like punctuation and whitespace as they are
    else:
      result += char

  return result