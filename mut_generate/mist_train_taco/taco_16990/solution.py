"""
QUESTION:
You'll be given a string of random characters (numbers, letters, and symbols). To decode this string into the key we're searching for: 

(1) count the number occurences of each ascii lowercase letter, and

(2) return an ordered string, 26 places long, corresponding to the number of occurences for each corresponding letter in the alphabet.

For example:
```python
'$aaaa#bbb*cc^fff!z' gives '43200300000000000000000001'
   ^    ^   ^  ^  ^         ^^^  ^                   ^
  [4]  [3] [2][3][1]        abc  f                   z
  
'z$aaa#ccc%eee1234567890' gives '30303000000000000000000001'
 ^  ^   ^   ^                    ^ ^ ^                    ^
[1][3] [3] [3]                   a c e                    z
```
Remember, the string returned should always be 26 characters long, and only count lowercase letters. 

Note: You can assume that each lowercase letter will appears a maximum of 9 times in the input string.
"""

from collections import Counter
from string import ascii_lowercase

def decode_key(input_string: str) -> str:
    """
    Decodes the input string into a 26-character string representing the count of each lowercase letter in the alphabet.

    Parameters:
    input_string (str): The string of random characters to be decoded.

    Returns:
    str: A 26-character string where each character represents the count of the corresponding lowercase letter in the alphabet.
    """
    cnt = Counter(input_string)
    return ''.join(str(cnt[letter]) for letter in ascii_lowercase)