"""
QUESTION:
The goal of this exercise is to convert a string to a new string where each character in the new string is `"("` if that character appears only once in the original string, or `")"` if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

## Examples
```
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
```

**Notes**

Assertion messages may be unclear about what they display in some languages. If you read `"...It Should encode XXX"`, the `"XXX"` is the expected result, not the input!
"""

def encode_duplicate_characters(word: str) -> str:
    """
    Encodes a string such that each character is replaced by '(' if it appears only once
    in the original string (case-insensitive), or ')' if it appears more than once.

    :param word: The input string to be encoded.
    :return: The encoded string.
    """
    lower_word = word.lower()
    return ''.join(['(' if lower_word.count(c) == 1 else ')' for c in lower_word])