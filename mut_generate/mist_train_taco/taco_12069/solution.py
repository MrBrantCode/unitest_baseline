"""
QUESTION:
Create a __moreZeros__ function which will __receive a string__ for input, and __return an array__ (or null terminated string in C) containing only the characters from that string whose __binary representation of its ASCII value__ consists of _more zeros than ones_. 

You should __remove any duplicate characters__, keeping the __first occurence__ of any such duplicates, so they are in the __same order__ in the final array as they first appeared in the input string.

Examples

            
All input will be valid strings of length > 0. Leading zeros in binary should not be counted.
"""

def more_zeros(s: str) -> list:
    results = []
    for letter in s:
        dec_repr = bin(ord(letter))[2:]
        if dec_repr.count('0') > dec_repr.count('1') and letter not in results:
            results.append(letter)
    return results