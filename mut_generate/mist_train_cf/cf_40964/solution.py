"""
QUESTION:
Write a function `extract_species_names` that takes a string `lbar` of space-separated species names and their corresponding FASTA file identifiers, and returns a list of unique species names. Each species name consists of alphabetic characters and underscores, and each FASTA file identifier consists of alphanumeric characters and underscores. The input string `lbar` has a length between 1 and 10^4. The function should return a list of unique species names, where each species name is the part of the string before the second underscore in each entry.
"""

from typing import List

def extract_species_names(lbar: str) -> List[str]:
    species_names = set()
    entries = lbar.split()
    for entry in entries:
        species_name = entry.split('_')[0]
        species_names.add(species_name)
    return list(species_names)