"""
QUESTION:
## Description

Welcome, Warrior! In this kata, you will get a message and you will need to get the frequency of each and every character!

## Explanation

Your function will be called `char_freq`/`charFreq`/`CharFreq` and you will get passed a string, you will then return a dictionary (object in JavaScript) with as keys the characters, and as values how many times that character is in the string. You can assume you will be given valid input. 

## Example

```python
char_freq("I like cats") // Returns {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1}
```
"""

from collections import Counter

def char_freq(message: str) -> dict:
    """
    Calculate the frequency of each character in the given message.

    Parameters:
    message (str): The input string for which character frequencies are to be calculated.

    Returns:
    dict: A dictionary with characters as keys and their respective frequencies as values.
    """
    return Counter(message)