"""
QUESTION:
Write a function called `check_symbol_count` that takes three arguments: a string `sequence`, a character `symbol`, and an integer `count`. The function should return `True` if `symbol` occurs exactly `count` times in `sequence`, and `False` otherwise.
"""

def check_symbol_count(sequence, symbol, count):
    return sequence.count(symbol) == count