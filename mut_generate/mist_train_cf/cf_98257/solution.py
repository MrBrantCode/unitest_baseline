"""
QUESTION:
Create a function named `decode_json` that takes an encoded string as input and returns the decoded string. The decoding process involves replacing specific characters with their corresponding decoded characters as per the given substitution code. 

The substitution code is as follows:
- A -> %
- B -> $
- C -> #
- D -> @
- E -> !
- F -> &
- G -> *
- H -> ^
- I -> <
- J -> >
- K -> (
- L -> )
- M -> _
- N -> +
- O -> -
- P -> =
- Q -> {
- R -> }
- S -> [
- T -> ]
- U -> :
- V -> ;
- W -> '
- X -> "
- Y -> \
- Z -> ~
- 0 -> ?
- 1 -> /
- 2 -> .
- 3 -> ,
- 4 -> ;
- 5 -> :
- 6 -> '
- 7 -> "
- 8 -> \
- 9 -> -

The function should handle all characters, including the ones not mentioned in the substitution code, by leaving them unchanged.
"""

def decode_json(encoded_data):
    substitution_code = {
        "%": "A", "$": "B", "#": "C", "@": "D", "!": "E", "&": "F", "*": "G", "^": "H", 
        "<": "I", ">": "J", "(": "K", ")": "L", "_": "M", "+": "N", "-": "O", "=": "P", 
        "{": "Q", "}": "R", "[": "S", "]": "T", ":": "U", ";": "V", "'": "W", "\"": "X", 
        "\\": "Y", "~": "Z", "?": "0", "/": "1", ".": "2", ",": "3", ";": "4", ":": "5", 
        "'": "6", "\"": "7", "\\": "8", "-": "9"
    }
    decoded_data = ""
    for char in encoded_data:
        if char in substitution_code:
            decoded_data += substitution_code[char]
        else:
            decoded_data += char
    return decoded_data