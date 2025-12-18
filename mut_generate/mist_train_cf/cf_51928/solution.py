"""
QUESTION:
Create a function `check_profanity(input_text)` that takes a string as input and returns a boolean value indicating whether the input text contains any abusive or vulgar words. The function should use a predefined list of profanity words and perform case-insensitive checking. The predefined list of profanity words can be extended as needed.
"""

def check_profanity(input_text):
    profanity_words = ["stupid", "moron", "jerk", "idiot"] # Add your list of vulgar or abusive words here
    for word in profanity_words:
        if word in input_text.lower(): # Convert the input to lower case for case-insensitive checking
            return True
    return False