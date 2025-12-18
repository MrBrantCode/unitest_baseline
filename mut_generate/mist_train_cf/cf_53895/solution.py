"""
QUESTION:
Implement a function `countVowelsInEncodedString(string)` that encodes an input string by replacing every character with the character that appears two places after it in the ASCII table, then counts and returns the number of vowels in the encoded string. The function should correctly handle both lowercase and uppercase letters, non-letter characters, and the transition for letters 'y' and 'z'.
"""

def countVowelsInEncodedString(string):
    vowels = 'aieouAIEOU'  
    encoded_string = ''
    for ch in string:
        # Check if character is a letter and encode it
        if ch.isalpha():
            encoded_string += chr((ord(ch.lower()) - 97 + 2) % 26 + 97) if ch.islower() else chr((ord(ch) - 65 + 2) % 26 + 65)
        # Keep non-letter characters as it is
        else:
            encoded_string += ch
    count = 0
    for letter in encoded_string:
        if letter in vowels:
            count += 1
    return count