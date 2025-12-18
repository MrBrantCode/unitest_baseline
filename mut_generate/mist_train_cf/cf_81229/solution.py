"""
QUESTION:
Write a function `text_transform` that takes a string `text` as input. The function should replace each letter in the text with its corresponding position in the English alphabet, where positions are represented as two-digit numbers (with a leading zero for single-digit positions). The function should handle special characters by leaving them unchanged and represent spaces as '00'.
"""

def text_transform(text):
    result = ""
    for char in text:
        if char.isalpha():
            num = ord(char.lower()) - 96
            result += "{:02d}".format(num)
        elif char == " ":
            result += "00"
        else:
            result += char
    return result