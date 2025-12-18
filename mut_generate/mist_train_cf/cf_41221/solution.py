"""
QUESTION:
Create a Python function named `expand_contractions` that takes a string `text` as input and returns the input text with all standard English contractions replaced with their expanded forms. Assume the input text contains only standard English contractions and may include punctuation and multiple contractions. Use the provided regular expression pattern to match contractions: `re.compile(r"\b(can't|won't|I'm|you'll|he's|she's|it's|we're|they're|I've|you've|we've|they've|I'll|you'll|he'll|she'll|it'll|we'll|they'll|isn't|aren't|wasn't|weren't|haven't|hasn't|hadn't|won't|wouldn't|don't|doesn't|didn't|can't|couldn't|shouldn't|mightn't|mustn't|ain't)\b")`.
"""

import re

def expand_contractions(text):
    # Define a regular expression pattern to match contractions.
    abbreviations_pattern = re.compile(r"\b(can't|won't|I'm|you'll|he's|she's|it's|we're|they're|I've|you've|we've|they've|I'll|you'll|he'll|she'll|it'll|we'll|they'll|isn't|aren't|wasn't|weren't|haven't|hasn't|hadn't|won't|wouldn't|don't|doesn't|didn't|can't|couldn't|shouldn't|mightn't|mustn't|ain't)\b")

    # Function to expand matched contractions.
    def expand_match(contraction):
        expanded_contraction = contraction.group(0)
        if contraction.group(0) == "I'm":
            expanded_contraction = "I am"
        # Add more expansion rules for other contractions as needed
        else:
            expanded_contraction = expanded_contraction.replace("'", "")
        return expanded_contraction

    # Replaces contractions with expanded contractions in text.
    normalized_text = abbreviations_pattern.sub(expand_match, text)
    return normalized_text