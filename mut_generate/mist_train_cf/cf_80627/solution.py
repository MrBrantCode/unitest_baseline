"""
QUESTION:
Write a function `shortest_completing_word` that takes a string `license_plate` and a list of strings `words` as input, and returns the shortest completing word in `words`. A completing word is a word that contains all the letters in `license_plate`, ignoring numbers and spaces, and treating letters as case insensitive. If a letter appears more than once in `license_plate`, then it must appear in the word the same number of times or more. If there are multiple shortest completing words, return the one that occurs in `words` with the least frequency. If there is still a tie, return the first one that occurs in `words`. 

Constraints: `1 <= license_plate.length <= 15`, `1 <= words.length <= 5000`, `1 <= words[i].length <= 20`.
"""

def shortest_completing_word(license_plate: str, words: list[str]) -> str:
    """
    Returns the shortest completing word in the list of words.
    
    A completing word is a word that contains all the letters in license_plate, 
    ignoring numbers and spaces, and treating letters as case insensitive. 
    If a letter appears more than once in license_plate, then it must appear 
    in the word the same number of times or more. If there are multiple shortest 
    completing words, return the one that occurs in words with the least frequency. 
    If there is still a tie, return the first one that occurs in words.
    """
    def char_frequency(string: str) -> dict:
        """
        Computes the frequency of characters in a string.
        """
        frequency = {}
        for char in string:
            if char.isalpha():
                frequency[char.lower()] = frequency.get(char.lower(), 0) + 1
        return frequency

    lp_freq = char_frequency(license_plate)
    solution, length = None, float('inf')

    for word in words:
        w_freq = char_frequency(word)
        if all(lp_freq[char] <= w_freq.get(char, 0) for char in lp_freq):
            if len(word) < length:
                solution, length = word, len(word)
    
    return solution