"""
QUESTION:
Create a function named `detect_plagiarism` that takes two parameters: a string of the document text and a list of strings representing the database of known plagiarized content. The function should return a boolean indicating whether the document text contains plagiarized content from the database.
"""

from difflib import SequenceMatcher

def detect_plagiarism(document, database):
    """
    Detect plagiarism in a document by comparing it to a database of known plagiarized content.

    Args:
    document (str): The text of the document to check for plagiarism.
    database (list): A list of strings representing the database of known plagiarized content.

    Returns:
    bool: True if the document contains plagiarized content, False otherwise.
    """

    # Iterate over each known plagiarized content in the database
    for plagiarized_content in database:
        # Calculate the similarity ratio between the document and the plagiarized content
        similarity_ratio = SequenceMatcher(None, document, plagiarized_content).ratio()
        
        # If the similarity ratio is greater than 0.5, consider it plagiarized
        if similarity_ratio > 0.5:
            return True

    # If no plagiarized content is found, return False
    return False