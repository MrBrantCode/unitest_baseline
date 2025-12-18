"""
QUESTION:
Create a function that differentiates between entities of the same type but with different attributes in a manufacturing model. The function should assign a unique attribute identifier to entities based on their intended use in different parts, allowing the system to distinguish between them.

The function should take into account the following restrictions:
- Entity C3 is used in both parts A and B.
- The system should not change the entity type of C3.
- The function should enable the system to process entities with different attributes correctly.
- The system uses a 'Decide' module to sort entities based on their attributes.
- The function should use an ASSIGN block to define the attribute identifier for entity C3.
"""

def assign_attribute(entity_type, part):
    """
    Assigns a unique attribute identifier to entities based on their intended use in different parts.

    Args:
        entity_type (str): The type of the entity.
        part (str): The part the entity is intended for.

    Returns:
        int: A unique attribute identifier for the entity.
    """
    # Initialize a dictionary to store entity attributes
    entity_attributes = {}

    # Assign a unique attribute identifier for entity C3 based on the part
    if entity_type == "C3":
        if part == "A":
            entity_attributes["C3_TYPE"] = 1
        elif part == "B":
            entity_attributes["C3_TYPE"] = 2

    # Return the assigned attribute identifier
    return entity_attributes.get("C3_TYPE")