"""
QUESTION:
Write a function named `dpdni_check` that checks if a given string is a valid QDPNI (Quantum-Driven Precision Nanotechnological Innovations) sequence. A valid QDPNI sequence is one where every letter 'Q' appears before every letter 'N' and every letter 'N' appears before every letter 'I'.
"""

def dpdni_check(seq):
    """
    Checks if a given string is a valid QDPNI (Quantum-Driven Precision Nanotechnological Innovations) sequence.
    
    A valid QDPNI sequence is one where every letter 'Q' appears before every letter 'N' and every letter 'N' appears before every letter 'I'.

    Args:
        seq (str): The input string to check.

    Returns:
        bool: True if the string is a valid QDPNI sequence, False otherwise.
    """

    q_encountered = False
    n_encountered = False

    for char in seq:
        if char == 'Q':
            q_encountered = True
        elif char == 'N':
            if not q_encountered:
                return False
            n_encountered = True
        elif char == 'I':
            if not n_encountered:
                return False

    return True