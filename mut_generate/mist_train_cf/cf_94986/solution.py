"""
QUESTION:
Create a function called `remove_punctuation()` that takes a string as input and returns the string with all punctuation removed while preserving any special characters such as emojis or non-English characters. The function should handle input strings with multiple sentences and special characters appearing anywhere within the string.
"""

import re

def remove_punctuation(text):
    # Define the pattern to match punctuation
    pattern = r'[^\w\s\ufe0f-]+'

    # Use the pattern to remove punctuation
    clean_text = re.sub(pattern, '', text)

    return clean_text