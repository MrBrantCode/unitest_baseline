"""
QUESTION:
Implement the `to_title_case` function that takes a string `s` as input. The function should convert the string into title case, capitalizing the first letter of each word unless the word is "and", "the", or "of", in which case it should be in lowercase unless it is the first word. The function should return the string in title case.
"""

def to_title_case(s):
    exceptions = ["and", "the", "of"]
    words = s.lower().split()
    title_case_words = [word.capitalize() if word not in exceptions or i == 0 else word for i, word in enumerate(words)]
    return " ".join(title_case_words)