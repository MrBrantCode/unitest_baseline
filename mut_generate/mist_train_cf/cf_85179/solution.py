"""
QUESTION:
Create a function named `digit_to_asterisk` that takes in a string `text` and a dictionary `replacement_dict` where keys are characters to be replaced and values are the corresponding replacement characters. The function should replace all occurrences of each key in the text with its corresponding value and return the modified string. If a key is not found in the text, it should print an error message. If a value in the dictionary is `None` or an empty string, it should print an error message.
"""

def digit_to_asterisk(text, replacement_dict):
    new_text = text
    invalid_chars = [None, ""]

    for key, value in replacement_dict.items():
        if key not in new_text:
            print(f"ERROR: The character {key} not found in the input string {text}.")
        elif value in invalid_chars:
            print(f"ERROR: Invalid replacement for {key}. Replacement cannot be None or an empty string.")
        else:
            new_text = new_text.replace(key, value)
    
    return new_text