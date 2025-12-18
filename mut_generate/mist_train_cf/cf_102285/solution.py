"""
QUESTION:
Create a function called `clarify_reply` that takes a user's reply as input and returns a clarification prompt if the reply is not a complete sentence, contains at least one punctuation mark (excluding question marks), or includes contractions or slang words. The input reply will be a string.
"""

import re

def clarify_reply(reply):
    """
    Returns a clarification prompt if the reply is not a complete sentence, 
    contains at least one punctuation mark (excluding question marks), 
    or includes contractions or slang words.

    Args:
        reply (str): The user's reply.

    Returns:
        str: A clarification prompt if the reply needs clarification, otherwise an empty string.
    """

    # Define a list of common contractions and slang words
    contractions_and_slang = ["don't", "won't", "can't", "shouldn't", "aren't", "isn't", "wasn't", "weren't", "didn't", "doesn't", "i'm", "you're", "he's", "she's", "it's", "we're", "they're", "lol", "btw", "imo", "tbh"]

    # Check if the reply contains any contractions or slang words
    if any(word in reply.lower() for word in contractions_and_slang):
        return "Please rephrase without using contractions or slang words."

    # Check if the reply contains at least one punctuation mark (excluding question marks)
    if re.search(r'[^\w\s\?\.,!]', reply) or re.search(r'[^\w\s?!\.]', reply):
        return "Please rephrase without using punctuation marks."

    # Check if the reply is not a complete sentence (i.e., it doesn't end with a period, question mark, or exclamation mark)
    if not reply.strip()[-1] in ['.', '?', '!']:
        return "Please provide a complete sentence."

    # If none of the above conditions are met, return an empty string
    return ""