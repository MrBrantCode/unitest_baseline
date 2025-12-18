"""
QUESTION:
# Description:

Remove the minimum number of exclamation marks from the start/end of each word in the sentence to make their amount equal on both sides.

### Notes:
* Words are separated with spaces
* Each word will include at least 1 letter
* There will be no exclamation marks in the middle of a word

___

## Examples

```
remove("Hi!") === "Hi"
remove("!Hi! Hi!") === "!Hi! Hi"
remove("!!Hi! !Hi!!") === "!Hi! !Hi!"
remove("!!!!Hi!! !!!!Hi !Hi!!!") === "!!Hi!! Hi !Hi!"
```
"""

import re

def balance_exclamation_marks(sentence: str) -> str:
    """
    Remove the minimum number of exclamation marks from the start/end of each word 
    in the sentence to make their amount equal on both sides.

    Parameters:
    - sentence (str): The input sentence containing words with exclamation marks.

    Returns:
    - str: The modified sentence where each word has an equal number of exclamation marks 
           at the start and end.
    """
    def balance_word(word):
        match = re.match(r'^(!*)(.*?)(!*)$', word)
        if match:
            left_exclamations, core, right_exclamations = match.groups()
            min_exclamations = min(len(left_exclamations), len(right_exclamations))
            return '!' * min_exclamations + core + '!' * min_exclamations
        return word

    return ' '.join(balance_word(word) for word in sentence.split())