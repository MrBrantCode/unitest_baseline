"""
QUESTION:
Write a function named `find_dependent_clause(sentence: str) -> Tuple[str, int]` that takes in a sentence as a string and returns a tuple containing the type of dependent clause ("restrictive" or "nonrestrictive") and the index position of the first character of the dependent clause in the sentence. The function should only consider the first dependent clause and return an empty string and -1 as the index position if there is no dependent clause. The sentence will always be a valid English sentence.
"""

import re
from typing import Tuple

def find_dependent_clause(sentence: str) -> Tuple[str, int]:
    """
    This function takes a sentence as input and returns a tuple containing the type of dependent clause 
    ("restrictive" or "nonrestrictive") and the index position of the first character of the dependent clause.
    
    Args:
    sentence (str): The input sentence to be analyzed.
    
    Returns:
    Tuple[str, int]: A tuple containing the type of dependent clause and its index position. 
                     If no dependent clause is found, it returns an empty string and -1.
    """

    # Define the keywords that mark the start of a dependent clause
    dependent_clause_keywords = ["that", "who", "which"]
    
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize variables to store the type and index of the dependent clause
    clause_type = ""
    index = -1
    
    # Iterate through the words in the sentence
    for i in range(len(words)):
        # Check if the current word is a dependent clause keyword
        if words[i].lower() in dependent_clause_keywords:
            # Determine if the dependent clause is restrictive or nonrestrictive
            if i > 0 and re.match(r'^[a-zA-Z]+$', words[i-1]):
                clause_type = "restrictive"
            else:
                clause_type = "nonrestrictive"
            
            # Calculate the index position of the dependent clause
            index = sentence.find(words[i])
            
            # Break the loop as we have found the first dependent clause
            break
    
    # Return the type and index of the dependent clause
    return clause_type, index