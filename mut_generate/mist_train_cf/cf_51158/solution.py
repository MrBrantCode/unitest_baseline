"""
QUESTION:
Create a function called `make_child_friendly` that takes a string of text as input and returns a new string with complex philosophical concepts replaced with child-friendly explanations. The function should use a dictionary to map complex words to their simpler equivalents. The input text will only contain spaces as separators, and the output should also be a string with spaces as separators.
"""

def make_child_friendly(text):
    complex_to_child_friendly = {"existentialism": "thinking about existence", "phenomenology": "how things appear to us"}
    words = text.split()
    child_friendly_text = ' '.join([complex_to_child_friendly.get(word, word) for word in words])
    return child_friendly_text