"""
QUESTION:
Write a function `harmonize_numerical_entities(entity1, entity2)` that takes two string representations of numbers as input, where `entity1` uses a comma as the decimal separator and `entity2` uses a period as the decimal separator. The function should convert both numbers to a uniform format (float) and return them.
"""

def harmonize_numerical_entities(entity1, entity2):
    """
    Convert two string representations of numbers to a uniform float format.
    
    Parameters:
    entity1 (str): Number with a comma as the decimal separator.
    entity2 (str): Number with a period as the decimal separator.
    
    Returns:
    tuple: Both numbers converted to float.
    """
    
    # replace ',' in first numerical entity with '.' and convert to float
    entity1 = float(entity1.replace(',', '.'))

    # convert second numerical entity to float
    entity2 = float(entity2)
    
    return entity1, entity2