"""
QUESTION:
Implement a function called `compress_string` that uses LZW compression algorithm to compress an input string and returns a compressed string. The compressed string should contain a maximum of 5 consecutive repeating characters in any cluster.
"""

def compress_string(s):
    """
    Compress an input string using LZW compression algorithm.

    Args:
    s (str): The input string to be compressed.

    Returns:
    str: The compressed string.
    """
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    w = ""
    result = []
    for c in s:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dictionary_size
            dictionary_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return ''.join(str(x) for x in result)