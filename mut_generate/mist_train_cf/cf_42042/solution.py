"""
QUESTION:
Create a function called `rec_sites` that takes two parameters: `dna_sequence` and `recognition_site`, both as strings. The function should count the occurrences of `recognition_site` within `dna_sequence` and return the total count as a string. The `dna_sequence` is a string of characters where each character represents a nucleotide (A, T, C, or G). The function should be registered as a custom template filter in Django.
"""

def rec_sites(dna_sequence, recognition_site):
    """
    Counts the occurrences of a recognition site within a DNA sequence.

    Args:
        dna_sequence (str): A string of characters representing nucleotides (A, T, C, or G).
        recognition_site (str): The site to be searched for within the DNA sequence.

    Returns:
        str: The total count of recognition sites as a string.
    """
    count = 0
    site_length = len(recognition_site)
    for i in range(len(dna_sequence) - site_length + 1):
        if dna_sequence[i:i + site_length] == recognition_site:
            count += 1
    return str(count)