"""
QUESTION:
Determine the final occurrence's location and repetition rate of a unique chain `s` within a given textual dataset `D`. The function, named `count_occurrences`, should take two parameters: `data` and `s`. It should return the number of occurrences and the position of the last occurrence of `s` in `data`. Note that string positions start from 0.
"""

def count_occurrences(data, s):
    """
    Determine the final occurrence's location and repetition rate of a unique chain `s` within a given textual dataset `D`.
    
    Args:
        data (str): The textual dataset.
        s (str): The unique chain.
    
    Returns:
        tuple: A tuple containing the number of occurrences and the position of the last occurrence of `s` in `data`.
    """
    num_occurrences = data.count(s)
    last_occurrence_pos = data.rfind(s)
    return num_occurrences, last_occurrence_pos