"""
QUESTION:
Create a function named `calculate_character_freq` that takes three phrases (phrase1, phrase2, phrase3) as input and returns a dictionary with each distinct character across the three phrases as keys and their total frequency count as values. The function should also calculate and print the number of distinct characters in each phrase. Maintain case-sensitivity and do not exclude any characters.
"""

def calculate_character_freq(phrase1, phrase2, phrase3):
    """
    Calculate the frequency of each character across three phrases and the number of distinct characters in each phrase.

    Args:
    phrase1 (str): The first phrase.
    phrase2 (str): The second phrase.
    phrase3 (str): The third phrase.

    Returns:
    dict: A dictionary with each distinct character as keys and their total frequency count as values.
    """
    
    all_phrases = phrase1 + phrase2 + phrase3
    freq_dict = {}
    
    for char in all_phrases:
        if char not in freq_dict:
            freq_dict[char] = all_phrases.count(char)
    
    distinct_chars_phrase1 = len(set(phrase1))
    distinct_chars_phrase2 = len(set(phrase2))
    distinct_chars_phrase3 = len(set(phrase3))
    
    print("Distinct Characters in Phrase 1: ", distinct_chars_phrase1)
    print("Distinct Characters in Phrase 2: ", distinct_chars_phrase2)
    print("Distinct Characters in Phrase 3: ", distinct_chars_phrase3)
    
    return freq_dict