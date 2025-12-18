"""
QUESTION:
Create a function named `enhanced_consonant_count` that takes a string `s` as input and returns the total count of consonants in the string, prioritizing the uncommon consonants in the order from 'z' to 'b'. The function should ignore case sensitivity and only count each consonant once per occurrence in the string.
"""

def enhanced_consonant_count(s: str) -> int:
    """
    Return the overall sum of consonants found in the input string.
    Count the most uncommon consonants first (starting from 'z' to 'b').
    """
    # define the consonants in an uncommon order
    consonants = 'zxcvbnmlkjhgfdstprq'
    count = 0
    
    # convert the string to lowercase
    s = s.lower()
    
    # iterate over each consonant in the uncommon order
    for con in consonants:
        count += s.count(con) 

    return count