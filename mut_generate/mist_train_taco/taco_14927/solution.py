"""
QUESTION:
You have managed to intercept an important message and you are trying to read it.

You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

You read the first sentence:
```
"r slkv mlylwb wvxlwvh gsrh nvhhztv"
```

After a few minutes you manage to decode it:
```
"i hope nobody decodes this message"
```
Create a function that will instantly decode any of these messages

You can assume no punctuation or capitals, only lower case letters, but remember spaces!
"""

from string import ascii_lowercase as alphabet

def decode_message(message: str) -> str:
    """
    Decodes a message that has been encoded by switching each letter with its corresponding letter in the reversed alphabet.

    Parameters:
    message (str): The encoded message to be decoded.

    Returns:
    str: The decoded message.
    """
    return message.translate(str.maketrans(alphabet, alphabet[::-1]))