"""
QUESTION:
Create a function `classify_entities` that takes an array of dictionaries as input. Each dictionary contains information about an entity, including a 'type' and a 'subAttributes' dictionary with a 'color' key. The function should return a nested dictionary where the outer keys are the unique 'type' values, the inner keys are the unique 'color' values, and the innermost values are lists of entities that match the corresponding 'type' and 'color'.
"""

def classify_entities(array):
    result = {}

    for entity in array:
        type_ = entity['type']
        color = entity['subAttributes']['color']

        # Initialize new dictionary for the type if it does not exist
        if type_ not in result:
            result[type_] = {}

        # Initialize new list for the color in the specific type dictionary if it does not exist
        if color not in result[type_]:
            result[type_][color] = []

        # Append the entity to the correct list
        result[type_][color].append(entity)

    return result