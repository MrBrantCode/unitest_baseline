"""
QUESTION:
Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be strings, and normal letters.
"""

def check_tail_fit(body: str, tail: str) -> bool:
    """
    Checks if the tail fits the body by comparing the last character of the body with the tail.

    Parameters:
    - body (str): The body of the animal.
    - tail (str): The tail of the animal.

    Returns:
    - bool: True if the last character of the body matches the tail, False otherwise.
    """
    return body.endswith(tail)