"""
QUESTION:
Write a function named `convert_to_proper_noun` that takes a string of commonly used technological terms as input and returns the term as a proper noun. The input terms may be separated by a hyphen. The output should capitalize the first letter of each word in the term. For example, "Wi-Fi" should be converted to "WiFi".
"""

def convert_to_proper_noun(tech_term):
    proper_noun = ""
    for word in tech_term.split("-"):
        proper_noun += word.capitalize()
    return proper_noun