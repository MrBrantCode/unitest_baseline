"""
QUESTION:
Create a function named `cipher` that takes two parameters: an input string and an integer key. The function should implement a Caesar Cipher encryption algorithm, shifting each letter in the input string by the specified key value. Non-alphabet characters should remain unchanged. The shift should wrap around the alphabet, so a shift of 1 would change 'z' to 'a' and 'Z' to 'A'.
"""

def cipher(input_str, key):
  output_str = ""

  for char in input_str:
    if char.isalpha():
      # Encrypt each character
      ascii_value = ord(char)
      ascii_value = ascii_value + (key % 26)
      if char.isupper():
        if ascii_value > ord("Z"):
          ascii_value -= 26
      elif char.islower():
        if ascii_value > ord("z"):
          ascii_value -= 26  
      output_str += chr(ascii_value)
    else:
      output_str += char

  return output_str