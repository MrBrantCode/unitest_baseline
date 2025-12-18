"""
QUESTION:
Write a function `check_text(text)` that checks if a given text contains a word that appears more than three times in a row and has at least one letter that appears only once in the entire text.
"""

def check_text(text):
    # Find all words that appear more than 3 times in a row
    matches = re.findall(r'\b(\w+)\b(?:\s+\1){2,}', text, re.IGNORECASE)
    # Find all letters that appear only once in the entire text
    unique_letters = set(filter(lambda x: text.count(x) == 1, set(text)))
    # Check if there's a word that appears more than 3 times in a row and has at least one unique letter
    for word in matches:
        if any(letter in unique_letters for letter in word):
            return True
    return False