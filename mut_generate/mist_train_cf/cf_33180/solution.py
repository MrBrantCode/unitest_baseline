"""
QUESTION:
Create a function `categorize_causes_of_death(causes)` that takes a list of causes of death as input, where each cause is a string in the format "action result". The function should return a dictionary where the keys are the unique actions and the values are lists of results associated with each action.
"""

def categorize_causes_of_death(causes):
    categorized_causes = {}
    for cause in causes:
        action, result = cause.split(' ', 1)
        action = action.rstrip('.,')  
        if action in categorized_causes:
            categorized_causes[action].append(result)
        else:
            categorized_causes[action] = [result]
    return categorized_causes