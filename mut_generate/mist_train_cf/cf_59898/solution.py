"""
QUESTION:
Develop a function `lexeme_recurrence_rate(lexeme, texts)` that calculates the recurrence rate of a given lexeme in a list of strings. The function should take a lexeme and a list of strings as input, count the occurrences of the lexeme in the list, and return the recurrence rate as the total count of the lexeme divided by the total number of words in the list. If the total number of words is zero, the function should return 0 to avoid division by zero.
"""

def lexeme_recurrence_rate(lexeme, texts):
    total_count = sum(text.count(lexeme) for text in texts)
    total_words = sum(len(text.split()) for text in texts)
    return total_count / total_words if total_words != 0 else 0