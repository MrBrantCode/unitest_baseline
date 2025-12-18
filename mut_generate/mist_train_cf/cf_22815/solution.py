"""
QUESTION:
Write a function `filter_documents` that takes a collection of documents as input and returns the documents where the "user_id" field is greater than 5, the "age" field is greater than or equal to 18, and the "name" field starts with the letter "A". The search for the letter "A" in the "name" field should be case-insensitive.
"""

import re

def filter_documents(documents):
    """
    Filters a collection of documents based on certain conditions.
    
    Args:
    documents (list): A list of dictionaries, each representing a document.
    
    Returns:
    list: A list of filtered documents.
    """
    filtered_documents = []
    for document in documents:
        if (document.get('user_id', 0) > 5 and 
            document.get('age', 0) >= 18 and 
            re.match('^A.*', document.get('name', ''), re.IGNORECASE)):
            filtered_documents.append(document)
    return filtered_documents