"""
QUESTION:
Create a function `custom_alphabet_sort(sequence: str) -> str` that takes a sequence as input and returns the sorted sequence based on a custom alphabet ordering. The custom alphabet ordering should prioritize the special characters for gaps (`-`) and stops (`*`), followed by the standard uppercase English letters, and then the generic letters (`X` and `N`).
"""

import string

def custom_alphabet_sort(sequence: str) -> str:
    gap_letter = "-"
    stop_letter = "*"
    generic_protein_letter = "X"
    generic_nt_letter = "N"
    every_letter_alphabet = string.ascii_uppercase

    custom_order = gap_letter + stop_letter + every_letter_alphabet + generic_protein_letter + generic_nt_letter
    sorted_sequence = sorted(sequence, key=lambda x: custom_order.index(x))
    return ''.join(sorted_sequence)