"""
QUESTION:
An AI has infected a text with a character!! 

This text is now **fully mutated** to this character.

If the text or the character are empty, return an empty string.  
There will never be a case when both are empty as nothing is going on!!

**Note:** The character is a string of length 1 or an empty string.

# Example
```python
text before = "abc"
character   = "z"
text after  = "zzz"
```
"""

def contaminate_text(text: str, char: str) -> str:
    """
    Mutates the given text by replacing all characters with the specified character.

    :param text: The original text to be mutated.
    :param char: The character to replace all characters in the text.
    :return: The mutated text.
    """
    if not text or not char:
        return ""
    return char * len(text)