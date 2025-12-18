"""
QUESTION:
Write a function `check_anagram_after_substitution(text1, text2, substitution1, substitution2)` that determines if two given texts `text1` and `text2` are anagrams after applying the given substitutions `substitution1` and `substitution2`, respectively. The substitutions are dictionaries where each key-value pair represents a character substitution. The function should consider capital letters and punctuation.
"""

def check_anagram_after_substitution(text1, text2, substitution1, substitution2):
    def generate_substituted_text(text, substitution):
        return ''.join(substitution.get(char, char) for char in text)

    substituted_text1 = generate_substituted_text(text1, substitution1)
    substituted_text2 = generate_substituted_text(text2, substitution2)

    return sorted(substituted_text1) == sorted(substituted_text2)