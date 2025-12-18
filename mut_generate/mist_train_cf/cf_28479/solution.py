"""
QUESTION:
Write a function named `relationship_not_equal` that takes two input parameters, `entity1` and `entity2`, and returns a boolean value indicating whether the relationship representations of `entity1` and `entity2` are not equal. The function should assume that the input entities are valid and have relationship representations that can be obtained using the `get_relationship_representation` method.
"""

def relationship_not_equal(entity1, entity2):
    return entity1.get_relationship_representation() != entity2.get_relationship_representation()