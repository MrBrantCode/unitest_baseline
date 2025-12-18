"""
QUESTION:
Take a sentence (string) and reverse each word in the sentence. Do not reverse the order of the words, just the letters in each word.

If there is punctuation, it should be interpreted as a regular character; no special rules.

If there is spacing before/after the input string, leave them there.

String will not be empty.

## Examples

```
"Hi mom" => "iH mom"
" A fun little challenge! " => " A nuf elttil !egnellahc "
```
"""

def reverse_words(sentence: str) -> str:
    """
    Reverses each word in the given sentence while maintaining the original order of words and any leading/trailing spaces.

    Parameters:
    sentence (str): The input sentence whose words need to be reversed.

    Returns:
    str: The sentence with each word reversed.
    """
    return ' '.join((word[::-1] for word in sentence.split(' ')))