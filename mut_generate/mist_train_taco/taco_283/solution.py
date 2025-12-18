"""
QUESTION:
Kontti language is a finnish word play game.

You add `-kontti` to the end of each word and then swap their characters until and including the first vowel ("aeiouy"); 

For example the word `tame` becomes `kome-tantti`; `fruity` becomes `koity-fruntti` and so on.

If no vowel is present, the word stays the same.

Write a string method that turns a sentence into kontti language!
"""

import re

def convert_to_kontti(sentence: str) -> str:
    """
    Converts a given sentence into Kontti language.

    Args:
        sentence (str): The input sentence to be converted.

    Returns:
        str: The sentence converted to Kontti language.
    """
    def kontti_word(word: str) -> str:
        """
        Converts a single word into Kontti language.

        Args:
            word (str): The input word to be converted.

        Returns:
            str: The word converted to Kontti language.
        """
        return re.sub('([^aeiouy]*[aeiouy])(.*)', 'ko\\2-\\1ntti', word, flags=re.I)
    
    return ' '.join([kontti_word(w) for w in sentence.split()])