"""
QUESTION:
Write a function named `word_counter` that takes in three parameters: `text`, `word`, and `case_sensitive`. The `word_counter` function should return the number of occurrences of the given `word` in the `text` based on the specified case sensitivity. The function should handle both case-sensitive and case-insensitive searches. If `case_sensitive` is `True`, the function should perform a case-sensitive search; otherwise, it should perform a case-insensitive search. The function should also handle edge cases such as empty input text or word.
"""

def word_counter(text, word, case_sensitive=True):
    if not text or not word:
        return 0

    if case_sensitive:
        return text.split().count(word)
    else:
        return text.lower().split().count(word.lower())