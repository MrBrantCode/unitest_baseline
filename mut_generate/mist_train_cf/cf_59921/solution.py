"""
QUESTION:
Develop a function named `text_subsequence_replacement` that takes three arguments: `primary_text`, `target_subsequence`, and `substitution_text`. The function should return `primary_text` with every instance of `target_subsequence` replaced by `substitution_text`, but only if `target_subsequence` is not part of a word. The function should be case sensitive and should not ignore leading or trailing whitespaces.
"""

import re

def text_subsequence_replacement(primary_text, target_subsequence, substitution_text):
    target_subsequence = re.escape(target_subsequence)  # Escape special regex characters
    pattern = r"\b({})\b".format(target_subsequence)  # Pattern to find the target subsequence
    primary_text = re.sub(pattern, substitution_text, primary_text)  # Replace the target subsequence
    return primary_text