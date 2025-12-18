"""
QUESTION:
Write a function `escape_quotes` that takes a string as input, and returns the string with all single quotes replaced with two single quotes, so it can be safely used in an Oracle SQL query. The function should not use any external libraries or database connections.
"""

def escape_quotes(input_string):
    """
    Escapes single quotes in a string by replacing them with two single quotes.
    
    Args:
    input_string (str): The input string to be processed.
    
    Returns:
    str: The input string with single quotes replaced with two single quotes.
    """
    return input_string.replace("'", "''")