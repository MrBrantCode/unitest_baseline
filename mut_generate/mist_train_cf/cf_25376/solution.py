"""
QUESTION:
Construct a decision tree that takes two features (color and texture) as input and outputs the type of fruit (mango or apple). The decision tree should only consider the following conditions: 
- Is it a mango? 
- Is it yellow? 
- Is it green? 
- Is it smooth?

Implement a function `fruit_classifier` that uses the decision tree to classify a fruit based on these conditions and returns the type of fruit.
"""

def fruit_classifier(color, texture, is_mango):
    """
    Classify a fruit based on its color, texture, and whether it's a mango.
    
    Parameters:
    color (str): Color of the fruit (e.g., yellow, green).
    texture (str): Texture of the fruit (e.g., smooth).
    is_mango (bool): Whether the fruit is a mango.
    
    Returns:
    str: Type of fruit (mango or apple) or 'Unknown' if it can't be classified.
    """
    if is_mango:
        return 'Mango'
    elif color == 'yellow':
        return 'Mango'
    elif color == 'green':
        if texture == 'smooth':
            return 'Apple'
        else:
            return 'Apple'
    else:
        if texture == 'smooth':
            return 'Apple'
        else:
            return 'Unknown'