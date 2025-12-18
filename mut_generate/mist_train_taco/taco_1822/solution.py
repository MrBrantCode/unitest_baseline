"""
QUESTION:
For building the encrypted string:Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:
```
"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
```

Write two methods:
```python
def encrypt(text, n)
def decrypt(encrypted_text, n)
```

```Fsharp
let encrypt (str:string) (n:int) -> string
let decrypt (str:string) (n:int) -> string
```

For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.

This kata is part of the Simple Encryption Series:
Simple Encryption #1 - Alternating Split
Simple Encryption #2 - Index-Difference
Simple Encryption #3 - Turn The Bits Around
Simple Encryption #4 - Qwerty

Have fun coding it and please don't forget to vote and rank this kata! :-)
"""

def encrypt(text: str, n: int) -> str:
    """
    Encrypts the input string by taking every 2nd character and concatenating it with the other characters,
    and repeating this process `n` times.

    :param text: The input string to be encrypted.
    :param n: The number of times to apply the encryption process.
    :return: The encrypted string.
    """
    if not text or n <= 0:
        return text
    
    for _ in range(n):
        text = text[1::2] + text[::2]
    
    return text

def decrypt(encrypted_text: str, n: int) -> str:
    """
    Decrypts the encrypted string by reversing the encryption process, and repeating this process `n` times.

    :param encrypted_text: The encrypted string to be decrypted.
    :param n: The number of times to apply the decryption process.
    :return: The decrypted string.
    """
    if not encrypted_text or n <= 0:
        return encrypted_text
    
    length = len(encrypted_text)
    ndx = length // 2
    
    for _ in range(n):
        a = encrypted_text[:ndx]
        b = encrypted_text[ndx:]
        encrypted_text = ''.join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    
    return encrypted_text