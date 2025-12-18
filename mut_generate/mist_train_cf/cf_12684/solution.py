"""
QUESTION:
Implement the `lzw_compress` function to compress a given string using LZW compression. The function should take a string as input and return the compressed string. The compressed string should be a comma-separated sequence of substrings, where each substring is a sequence of characters from the original string. The function should work for strings containing repeating characters in larger clusters.
"""

def lzw_compress(s):
    """
    Compress a given string using LZW compression.

    Args:
    s (str): The input string to be compressed.

    Returns:
    str: The compressed string, a comma-separated sequence of substrings.
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
    return ', '.join(str(x) for x in result)