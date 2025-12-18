"""
QUESTION:
Design a function called `unicode_converter` that takes a string of decimal numbers separated by commas as input. The input string may contain leading or trailing spaces, and the numbers will always be valid decimal numbers within the range of Unicode characters (0-65535). The function should return a string with the corresponding Unicode characters separated by spaces, skipping any invalid numbers and displaying an error message for them.
"""

def unicode_converter(input_string):
    unicode_chars = []
    if input_string:
        numbers = input_string.strip().split(", ")
        for num in numbers:
            try:
                if 0 <= int(num) <= 65535:
                    unicode_chars.append(chr(int(num)))
                else:
                    print("Invalid number:", num)
            except ValueError:
                print("Invalid number:", num)
    
    return " ".join(unicode_chars)