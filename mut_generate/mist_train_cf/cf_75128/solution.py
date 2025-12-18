"""
QUESTION:
Determine if two strings can be transformed into each other by swapping any two existing characters or transforming every occurrence of one existing character into another existing character.

Create a function `closeStrings(word1: str, word2: str)` that takes two strings as input and returns `True` if `word1` and `word2` can be transformed into each other, and `False` otherwise. Additionally, create a function `opCount(word1: str, word2: str)` that returns the minimum number of operations required to transform `word1` into `word2` if they can be transformed.

Restrictions:
- `1 <= word1.length, word2.length <= 10^5`
- `word1` and `word2` contain only lowercase English letters.
"""

from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    counter1, counter2 = Counter(word1), Counter(word2)
    return set(word1) == set(word2) and sorted(counter1.values()) == sorted(counter2.values())