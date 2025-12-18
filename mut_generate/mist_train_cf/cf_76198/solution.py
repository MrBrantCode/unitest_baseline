"""
QUESTION:
Create a function `shortest_string` that takes three string arguments. The function should remove all vowels from each string and return the shortest resulting string. The function is case-sensitive and considers both lowercase and uppercase vowels.
"""

def shortest_string(s1, s2, s3):
    """
    Removes all vowels from each input string and returns the shortest resulting string.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        s3 (str): The third input string.

    Returns:
        str: The shortest string after removing vowels.
    """
    strings = [s1, s2, s3]
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(strings)):
        for vowel in vowels:
            strings[i] = strings[i].replace(vowel, '')
    return min(strings, key=len)