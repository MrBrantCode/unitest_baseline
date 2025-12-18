"""
QUESTION:
Create a function `consonant_count_and_common` that takes a string `s` as input and returns a tuple containing the total count of consonants in the string and the most commonly occurring consonant. If there is a tie, return the consonant that comes first alphabetically. The function should be case-insensitive and return (0, None) if no consonants are found in the string.
"""

import collections
from typing import Tuple

def consonant_count_and_common(s: str) -> Tuple[int, str]:
    s = s.lower()  # lower case to ensure it works for both cases
    consonants = [char for char in s if char in 'bcdfghjklmnpqrstvwxyz']  # list of consonants in s

    if not consonants:
        return 0, None  # if no consonants found

    counter = collections.Counter(consonants)  # count the frequency of each consonant

    common_consonants = [k for k, c in counter.items() if c == max(counter.values())]  # Get keys with max value

    common_consonants.sort()  # sort to get the first alphabetically 

    return len(consonants), common_consonants[0]