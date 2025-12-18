"""
QUESTION:
Write a function `extract_lexical_entities` that takes a string as input, breaks it down into separate lexical entities (words) by removing extra whitespace, and returns a list of these entities. The function should also be able to return the number of extra whitespace characters removed from the input string.
"""

def extract_lexical_entities(input_string):
    """
    Breaks down the input string into separate lexical entities (words) by removing extra whitespace
    and returns a list of these entities along with the number of extra whitespace characters removed.

    Args:
        input_string (str): The input string to be processed.

    Returns:
        list, int: A list of lexical entities and the number of extra whitespace characters removed.
    """
    # Remove leading and trailing spaces
    stripped_string = input_string.strip()

    # Split the string into separate lexical entities
    lexical_entities = stripped_string.split()

    # Find the number of void textual elements (extra whitespace characters)
    void_elements = len(input_string) - len(stripped_string)

    return lexical_entities, void_elements