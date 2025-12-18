"""
QUESTION:
Write function ```wordsToSentence``` which will create a string from a list of strings, separated by space.

Example:

```["hello", "world"] -> "hello world"```
"""

def words_to_sentence(words: list[str]) -> str:
    return ' '.join(words)