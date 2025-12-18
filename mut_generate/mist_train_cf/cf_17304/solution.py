"""
QUESTION:
Implement a function `normalize_text` that takes a string `text` as input and returns the normalized version of the text. The normalization should include the following steps: 
- Converting all characters to lowercase.
- Removing all punctuation marks.
- Removing all numbers.
- Removing any leading or trailing white spaces.
- Replacing all consecutive spaces with a single space.
 
Use only built-in Python libraries for this implementation, without relying on any external libraries or packages specifically designed for natural language processing or text normalization.
"""

import string

def normalize_text(text):
    # Convert all characters to lowercase
    text = text.lower()
    
    # Remove all punctuation marks
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Remove all numbers
    text = ''.join([i for i in text if not i.isdigit()])
    
    # Remove any leading or trailing white spaces
    text = text.strip()
    
    # Replace all consecutive spaces with a single space
    text = ' '.join(text.split())
    
    return text