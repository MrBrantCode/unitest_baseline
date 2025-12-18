"""
QUESTION:
Write a function `correlate_wikipedia_measures` to calculate the correlation between the number of Wikipedia pages an entity has been translated to and the number of links that point to that page. The function should take in a list of entities, each represented as a tuple of `(entity_name, links, translated_pages)`. The function should return a correlation coefficient value representing the degree of relation between the two measures.
"""

import numpy as np

def correlate_wikipedia_measures(entities):
    """
    Calculate the correlation between the number of Wikipedia pages an entity has been translated to 
    and the number of links that point to that page.

    Args:
        entities (list): A list of entities, each represented as a tuple of 
                         (entity_name, links, translated_pages)

    Returns:
        float: A correlation coefficient value representing the degree of relation between the two measures
    """
    # Extract links and translated_pages from the entities list
    links = [entity[1] for entity in entities]
    translated_pages = [entity[2] for entity in entities]

    # Calculate the correlation coefficient using Pearson Correlation Coefficient
    correlation_coefficient = np.corrcoef(links, translated_pages)[0, 1]

    return correlation_coefficient