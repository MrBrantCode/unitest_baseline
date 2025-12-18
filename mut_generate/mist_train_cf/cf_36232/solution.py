"""
QUESTION:
Implement the `titlecase` function, which takes a string `s` and an optional string `minor_words` as input. The function should convert the string `s` into title case, where the first letter of each word is capitalized except for minor words, which should remain in lowercase unless they are the first word in the string. The function should handle special cases such as words with apostrophes and hyphens. The string `minor_words` is a space-separated list of minor words. If `minor_words` is not provided, it defaults to an empty string.

The input string `s` is 1 to 1000 characters long. The function should return the title-cased version of `s` as a string.
"""

def titlecase(s: str, minor_words: str = '') -> str:
    if not s:
        return ''

    minor_words = minor_words.lower().split()
    title_cased = [word.capitalize() if word.lower() not in minor_words or i == 0 else word.lower() for i, word in enumerate(s.split())]
    return ' '.join(title_cased)