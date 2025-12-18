"""
QUESTION:
The four bases found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

In genetics, GC-content is the percentage of Guanine (G) and Cytosine (C) bases on a DNA molecule that are either guanine or cytosine. 

Given a DNA sequence (a string) return the GC-content in percent, rounded up to 2 decimal digits for Python, not rounded in all other languages.

For more information about GC-content you can take a look to [wikipedia GC-content](https://en.wikipedia.org/wiki/GC-content).

**For example**: the GC-content of the following DNA sequence is 50%:
"AAATTTCCCGGG".

**Note**: You can take a look to my others bio-info kata [here](http://www.codewars.com/users/nbeck/authored)
"""

def calculate_gc_content(dna_sequence: str) -> float:
    """
    Calculate the GC-content of a given DNA sequence.

    Parameters:
    dna_sequence (str): The DNA sequence for which the GC-content is to be calculated.

    Returns:
    float: The GC-content percentage, rounded to 2 decimal places.
    """
    if not dna_sequence:
        return 0.0
    
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    gc_content_percentage = (gc_count / len(dna_sequence)) * 100
    
    return round(gc_content_percentage, 2)