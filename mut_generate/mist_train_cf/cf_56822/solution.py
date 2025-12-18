"""
QUESTION:
Create a function called `obfuscate_text` that takes two parameters: `input_text` (a string) and `lexemes_to_obfuscate` (a list of strings). The function should return the `input_text` with all occurrences of the lexemes in `lexemes_to_obfuscate` replaced with '***'.
"""

def obfuscate_text(input_text, lexemes_to_obfuscate):
    for lexeme in lexemes_to_obfuscate:
        input_text = input_text.replace(lexeme, '***')
    return input_text