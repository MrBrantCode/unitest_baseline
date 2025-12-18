"""
QUESTION:
## Description:

 Remove all exclamation marks from the end of words. Words are separated by spaces in the sentence.

### Examples

```
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi Hi"
remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"
```
"""

def remove_trailing_exclamations(sentence: str) -> str:
    """
    Remove all exclamation marks from the end of words in the given sentence.

    Parameters:
    - sentence (str): The input sentence from which trailing exclamation marks need to be removed from each word.

    Returns:
    - str: The modified sentence with all trailing exclamation marks removed from each word.
    """
    return ' '.join((w.rstrip('!') or w for w in sentence.split()))