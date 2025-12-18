"""
QUESTION:
Write a function called `eliminate_strings` that takes a list of strings as input and returns a new list containing only the strings that do not have the substring "regardless of" (case-sensitive or case-insensitive).
"""

def eliminate_strings(sequence_list):
    return [s for s in sequence_list if "regardless of" not in s.lower()]