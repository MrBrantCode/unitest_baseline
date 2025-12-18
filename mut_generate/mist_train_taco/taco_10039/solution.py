"""
QUESTION:
When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
"""

def number_to_word(n: int) -> str:
    """
    Converts a number between 0 and 9 into its corresponding word form.

    Parameters:
    n (int): The number to be converted (0-9).

    Returns:
    str: The word form of the number.
    """
    return ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][n]