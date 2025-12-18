"""
QUESTION:
Implement a function named `EntityComparator` that compares two entities based on their properties and returns an integer value indicating their relative status. The function should take into account the weights or priorities of different properties. The function should return 0 if the entities have equal status, a positive value if the first entity is more dominant, and a negative value if the second entity is more dominant. The function should be able to handle entities with different properties and weights. The properties and their corresponding weights should be passed as dictionaries.
"""

def EntityComparator(entity1, entity2, weights):
    """
    Compare two entities based on their properties and weights.

    Args:
    entity1 (dict): The first entity.
    entity2 (dict): The second entity.
    weights (dict): The weights or priorities of different properties.

    Returns:
    int: A value indicating the relative status of the entities.
    """
    score = 0
    for prop, weight in weights.items():
        score += weight * (entity1.get(prop, 0) - entity2.get(prop, 0))
    return score