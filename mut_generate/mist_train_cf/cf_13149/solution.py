"""
QUESTION:
Construct a decision tree to classify a fruit as mango or apple based on its characteristics. The function should take the color, texture, size, and weight of the fruit as input and return 'mango' or 'apple'. The classification should be determined by the following rules: 
- If the color is 'Red' or 'Green', classify as 'apple'.
- If the color is 'Yellow' or 'Orange', check the texture. If the texture is 'Smooth', classify as 'mango'. If the texture is 'Rough', check the size. If the size is 'Large', classify as 'mango'. If the size is 'Small' or 'Medium', check the weight. If the weight is 'Light', classify as 'mango'. If the weight is 'Heavy', classify as 'apple'.
"""

def classify_fruit(color, texture, size, weight):
    """
    Classify a fruit as 'mango' or 'apple' based on its characteristics.

    Args:
    color (str): The color of the fruit.
    texture (str): The texture of the fruit.
    size (str): The size of the fruit.
    weight (str): The weight of the fruit.

    Returns:
    str: The classification of the fruit as 'mango' or 'apple'.
    """

    # If the color is 'Red' or 'Green', classify as 'apple'
    if color in ['Red', 'Green']:
        return 'apple'

    # If the color is 'Yellow' or 'Orange', check the texture
    if color in ['Yellow', 'Orange']:
        # If the texture is 'Smooth', classify as 'mango'
        if texture == 'Smooth':
            return 'mango'
        
        # If the texture is 'Rough', check the size
        if texture == 'Rough':
            # If the size is 'Large', classify as 'mango'
            if size == 'Large':
                return 'mango'
            
            # If the size is 'Small' or 'Medium', check the weight
            if size in ['Small', 'Medium']:
                # If the weight is 'Light', classify as 'mango'
                if weight == 'Light':
                    return 'mango'
                # If the weight is 'Heavy', classify as 'apple'
                if weight == 'Heavy':
                    return 'apple'