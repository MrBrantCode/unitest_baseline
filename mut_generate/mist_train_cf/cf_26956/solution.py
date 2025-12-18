"""
QUESTION:
Implement a function named `calculate_average_scores` that takes a dictionary with tuples of three integers as keys and floating-point numbers as values. The function should return a dictionary where the keys are the first integers of the tuples and the values are the average of the corresponding floating-point numbers. If a key has no associated values, its average should be 0.0.
"""

def calculate_average_scores(scores_dict):
    category_scores = {}
    category_counts = {}
    
    for key, value in scores_dict.items():
        category = key[0]
        if category in category_scores:
            category_scores[category] += value
            category_counts[category] += 1
        else:
            category_scores[category] = value
            category_counts[category] = 1
    
    average_scores = {category: category_scores.get(category, 0.0) / category_counts.get(category, 1) for category in category_scores}
    
    return average_scores