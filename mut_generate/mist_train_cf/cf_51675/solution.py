"""
QUESTION:
Given a string representing a binary number, write a function called `is_valid_superposition` that returns True if the string can represent a superposition state (i.e., it contains at least one '0' and at least one '1') and False otherwise.
"""

def is_valid_superposition(s):
    return '0' in s and '1' in s