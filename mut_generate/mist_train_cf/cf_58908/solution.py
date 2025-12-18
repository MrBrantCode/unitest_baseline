"""
QUESTION:
Design a data model that allows for extensible and customizable form fields without requiring changes to the underlying database schema. The data model should be able to handle the addition and removal of form fields dynamically. Implement a function `entity_attribute_value_model` that can be used to store and retrieve entity-attribute-value pairs in a database.
"""

def entity_attribute_value_model(entity_id, attribute_name, value, db=None):
    """
    Stores and retrieves entity-attribute-value pairs in a database.

    Args:
    - entity_id (str): Unique identifier for the entity.
    - attribute_name (str): Name of the attribute.
    - value (str): Value of the attribute.
    - db (dict, optional): In-memory database. Defaults to None.

    Returns:
    - str: Value associated with the entity-attribute pair.
    """
    if db is None:
        db = {}

    # Initialize the entity in the database if it doesn't exist
    if entity_id not in db:
        db[entity_id] = {}

    # Store the attribute-value pair in the database
    db[entity_id][attribute_name] = value

    # Return the stored value
    return db[entity_id][attribute_name]