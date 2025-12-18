"""
QUESTION:
Create a function named `rot13` that takes a string `text` as input and applies the ROT13 substitution cipher method. The function should be able to handle strings containing special characters and numbers. The ROT13 cipher should work as follows: 
- For alphabets (both lowercase and uppercase), shift the characters 13 places to the right in the alphabet, wrapping around to the beginning if necessary.
- For numbers (0-9), apply a similar shifting scheme where 0-4 are shifted to 5-9 and 5-9 are shifted to 0-4.
The function should be able to both encode and decode the input string.
"""

def rot13(text):
    result = ""

    for v in text:
        char = v

        if ('a' <= v and v <= 'z'):
            if (char >= 'n'):
                char = chr(ord(char) - 13)
            else:
                char = chr(ord(char) + 13)

        elif ('A' <= v and v <= 'Z'):
            if (char >= 'N'):
                char = chr(ord(char) - 13)
            else:
                char = chr(ord(char) + 13)

        elif ('0' <= v and v <= '9'):
            if (int(char) >= 5):
                num = int(char) - 5
            else:
                num = int(char) + 5
            char = str(num)

        result += char

    return result