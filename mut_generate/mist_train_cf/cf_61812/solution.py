"""
QUESTION:
Create a function named `count_whitespace` that takes a string `input_text` as input and returns the number of Unicode whitespace characters within the string. The function should consider all Unicode whitespace characters, including but not limited to spaces, tabs, line feeds, and non-breaking spaces.
"""

import re

def count_whitespace(input_text):
    # Unicode whitespace characters
    unicode_whitespace = [
        '\u0009', # CHARACTER TABULATION
        '\u000A', # LINE FEED (LF)
        '\u000B', # LINE TABULATION
        '\u000C', # FORM FEED (FF)
        '\u000D', # CARRIAGE RETURN (CR)
        '\u0020', # SPACE
        '\u0085', # NEXT LINE (NEL)
        '\u00A0', # NO-BREAK SPACE
        '\u1680', # OGHAM SPACE MARK
        '\u2000', # EN QUAD
        '\u2001', # EM QUAD
        '\u2002', # EN SPACE
        '\u2003', # EM SPACE
        '\u2004', # THREE-PER-EM SPACE
        '\u2005', # FOUR-PER-EM SPACE
        '\u2006', # SIX-PER-EM SPACE
        '\u2007', # FIGURE SPACE
        '\u2008', # PUNCTUATION SPACE
        '\u2009', # THIN SPACE
        '\u200A', # HAIR SPACE
        '\u2028', # LINE SEPARATOR
        '\u2029', # PARAGRAPH SEPARATOR
        '\u202F', # NARROW NO-BREAK SPACE
        '\u205F', # MEDIUM MATHEMATICAL SPACE
        '\u3000', # IDEOGRAPHIC SPACE
    ]

    whitespace_pattern = "|".join(unicode_whitespace)
    whitespace_count = len(re.findall(whitespace_pattern, input_text))

    return whitespace_count