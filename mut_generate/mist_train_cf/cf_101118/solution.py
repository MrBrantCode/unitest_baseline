"""
QUESTION:
Create a function named `convert_to_proper_noun` that takes a string of a technological term as input and returns its proper noun form. The proper noun form should capitalize the first letter of each word in the term. For example, "Wi-Fi" should be converted to "WiFi." The function should handle terms with multiple words separated by hyphens or other separators.
"""

def convert_to_proper_noun(tech_term):
    proper_noun = ""
    for word in tech_term.replace("-", " ").split():
        proper_noun += word.capitalize()
    return proper_noun