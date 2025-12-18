"""
QUESTION:
Write a function `compare_sorting_orders` that takes a list of distinct text entities as input and returns the sorted lists based on the English alphabetic system and the ASCII system. The function should be case-sensitive and handle numeric values, symbols, and white spaces properly. It should also identify and report any differences between the two sorted orders.
"""

def compare_sorting_orders(text_entities):
    """
    This function compares the sorting orders of a list of distinct text entities 
    based on the English alphabetic system and the ASCII system.

    Args:
        text_entities (list): A list of distinct text entities.

    Returns:
        tuple: A tuple containing two lists. The first list is sorted based on 
        the English alphabetic system, and the second list is sorted based on 
        the ASCII system.
    """

    # For the English alphabetic system, convert the case to lower for sorting
    english_order = sorted(text_entities, key=lambda x: x.lower())
    # For the ASCII system, use the default behavior of the sorted function
    ascii_order = sorted(text_entities)

    return english_order, ascii_order