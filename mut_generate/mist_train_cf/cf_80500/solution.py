"""
QUESTION:
Create a function called `heaviest_combination` that takes a list of object names, a list of corresponding object weights, and a weight limit. Return the combination of objects that results in the heaviest weight without exceeding the given limit. The function should be able to handle any number of objects and any weight limit. The objects and weights should be represented as lists of equal length, and the weights should be non-negative numbers. The weight limit should also be a non-negative number.
"""

def heaviest_combination(objects, weights, limit):
    """
    Returns the combination of objects that results in the heaviest weight without exceeding the given limit.
    
    Args:
        objects (list): A list of object names.
        weights (list): A list of corresponding object weights.
        limit (float): A weight limit.
    
    Returns:
        list: The heaviest combination of objects within the limit.
    """
    # Initialize variables to remember the best combination
    best_weight = 0
    best_combination = []

    # Try all combinations
    for i in range(2**len(objects)):
        # Initialize variables for this combination
        combination = []
        weight = 0
        
        # Try adding each object
        for j in range(len(objects)):
            # If the jth bit of i is 1, add the object
            if (i >> j) & 1:
                combination.append(objects[j])
                weight += weights[j]
        
        # If this combination is heavier but not too heavy, remember it
        if weight > best_weight and weight <= limit:
            best_weight = weight
            best_combination = combination

    return best_combination