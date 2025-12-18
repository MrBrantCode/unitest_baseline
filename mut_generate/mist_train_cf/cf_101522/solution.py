"""
QUESTION:
Create a Python function named `repeat_string` that takes two parameters: a string `word` and an integer `n`. The function should return a JSON string containing the repeated string, the character count, and the ratio of vowels to consonants. The repeated string is created by concatenating the original input `n` times. The function should only accept `n` values between 1 and 100 inclusive.
"""

import json
def repeat_string(word: str, n: int) -> str:
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    count = {'vowels': 0, 'consonants': 0}
    
    for char in word:
        if char in vowels:
            count['vowels'] += 1
        elif char in consonants:
            count['consonants'] += 1
    
    ratio = count['vowels'] / count['consonants'] if count['consonants'] != 0 else 0
    
    if n < 1 or n > 100:
        return "Error: Integer parameter must be between 1 and 100 inclusive."
    
    repeated_word = word * n
    
    output = {
        'repeated_word': repeated_word,
        'character_count': len(repeated_word),
        'vowel_consonant_ratio': ratio
    }
    
    return json.dumps(output)