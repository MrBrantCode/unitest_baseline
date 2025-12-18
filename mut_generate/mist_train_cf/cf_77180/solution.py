"""
QUESTION:
Create a decision tree classifier function `build_decision_tree` for the given data points with 'Height' and 'Weight' features and 'Label' as the target variable. The function should take no arguments. The decision tree should be able to classify new data points based on their 'Height' and 'Weight'. The decision tree can be constructed based on the given conditions: 

- If the height is 5 ft, check the weight. If the weight is <= 130, classify as A, if the weight is > 140, classify as A, and if the weight is between 130 and 140, classify as B. 
- If the height is 6 ft, check the weight. If the weight is <= 130, classify as B, if the weight is > 140, classify as B, and if the weight is between 130 and 140, classify as A.
"""

def build_decision_tree(height, weight):
    """
    A decision tree classifier function to classify data points based on 'Height' and 'Weight'.

    Parameters:
    height (float): Height in ft.
    weight (float): Weight.

    Returns:
    str: The predicted class.
    """

    # Check height
    if height == 5:
        # Check weight
        if weight <= 130 or weight > 140:
            return 'A'
        else:
            return 'B'
    elif height == 6:
        # Check weight
        if weight <= 130 or weight > 140:
            return 'B'
        else:
            return 'A'
    else:
        # Handle unknown height
        return 'Unknown'