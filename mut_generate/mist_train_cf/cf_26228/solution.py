"""
QUESTION:
Format the input string according to the specified condition. The function should be named `capitalize_title`. The input string is a comma-separated string where each word is in lowercase. The output should be a string where each word's first letter is capitalized, and words are separated by underscores instead of commas.
"""

def capitalize_title(s):
    return "_".join(word.capitalize() for word in s.split(","))