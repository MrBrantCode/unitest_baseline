"""
QUESTION:
Write a function `check_anagram_segments(text: str) -> bool` that determines whether it is possible to divide the input string into two or more segments that are anagrams of one another. The function should consider an anagram as a word or phrase formed by reordering the letters of a different word or phrase, typically using all the original letters exactly once.
"""

def check_anagram_segments(text: str) -> bool:
    """
    Given an input string, the function determines whether it is possible to 
    divide the string into two or more segments that are anagrams of one another. 

    Anagrams are words or phrases formed by reordering the letters of a different word or phrase, 
    typically using all the original letters exactly once.

    The function counts the frequency of each unique character in the string and stores it in a dictionary. 
    If all frequencies are even number then the function returns True as the string can be divided into 
    two or more segments that are anagrams of one another. 
    
    But if there is more than one character with an odd count frequency, then the function returns False
    as it is not possible to divide the string into segments that are anagrams of one another. 

    Parameters:
    text (str): The string to check for anagram segments

    Returns:
    bool: True if the string can be divided into anagram segments, False otherwise.
    """

    # count the frequency of each unique character in the string
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # count characters with odd count frequency
    count_odd = sum(1 for count in frequency.values() if count % 2)

    return count_odd <= 1