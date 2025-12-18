"""
QUESTION:
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

```python
DNA_strand ("ATTGC") # return "TAACG"

DNA_strand ("GTAT") # return "CATA"
```
"""

def get_complementary_dna(dna_strand: str) -> str:
    """
    Returns the complementary DNA strand for the given DNA strand.

    Parameters:
    dna_strand (str): The DNA strand for which the complementary strand is to be found.

    Returns:
    str: The complementary DNA strand.
    """
    pairs = [('A', 'T'), ('C', 'G')]
    replacing_rules = pairs_to_dict(pairs)
    return ''.join([replacing_rules[nucleotide] for nucleotide in dna_strand])

def pairs_to_dict(pairs):
    """
    Converts a list of pairs into a dictionary where each element in the pair maps to its complement.

    Parameters:
    pairs (list of tuples): A list of tuples where each tuple contains a pair of complementary nucleotides.

    Returns:
    dict: A dictionary where each nucleotide maps to its complement.
    """
    d = {}
    for pair in pairs:
        d[pair[0]] = pair[1]
        d[pair[1]] = pair[0]
    return d