"""
QUESTION:
Create two functions, `string_to_binary(s)` and `binary_to_string(s)`, that convert a given string to its binary representation and back to the original string, respectively. The binary representation should be a string of 0s and 1s, with each character of the original string represented by 8 bits (or 1 byte) in binary. The functions should work with any string, including those containing punctuation and spaces.
"""

def string_to_binary(s):
  binary_string = ''
  for c in s:
    binary_string += bin(ord(c))[2:].zfill(8)  # zfill to ensure 8-bit binary
  return binary_string

def binary_to_string(s):
  text = ''
  for i in range(0, len(s), 8):  # step by 8 because each character is 8-bit long in ASCII
    binary = s[i:i+8]
    text += chr(int(binary, 2))  # convert 8-bit binary to integer then to Unicode character
  return text