"""
QUESTION:
Create a function named `sort_compilations` that takes two lists, `numeric_compilation` and `word_compilation`, as input. The function should sort `numeric_compilation` in ascending order and `word_compilation` in lexicographical order, and return the sorted lists. The function should not take any additional arguments.
"""

def sort_compilations(numeric_compilation, word_compilation):
    """
    Sorts numeric_compilation in ascending order and word_compilation in lexicographical order.

    Args:
        numeric_compilation (list): A list of numbers.
        word_compilation (list): A list of words.

    Returns:
        tuple: A tuple containing the sorted numeric_compilation and word_compilation lists.
    """
    numeric_compilation.sort()
    word_compilation.sort()
    return numeric_compilation, word_compilation