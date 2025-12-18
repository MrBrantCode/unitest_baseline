"""
QUESTION:
Write a function called `modify_dismax_query` that takes a query string as input, removes parentheses, and returns the modified query string. The function should be able to handle strings with parentheses and no parentheses. The modified query string should be compatible with the Dismax query parser in Solr.
"""

def modify_dismax_query(query_string):
    """
    Removes parentheses from a query string to make it compatible with the Dismax query parser in Solr.
    
    Parameters:
    query_string (str): The input query string.
    
    Returns:
    str: The modified query string without parentheses.
    """
    return query_string.replace("(", "").replace(")", "")