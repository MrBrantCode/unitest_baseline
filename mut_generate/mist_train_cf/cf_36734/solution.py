"""
QUESTION:
Implement a class method `entity_contains` to check if a given `entity` contains a specified `search` term, and a method `search_entities` to iterate over a collection of `entities` and yield those that contain a given `search` term. The `entity_contains` method should return `True` if the `search` term is found in the `entity` and `False` otherwise. The `search_entities` method should use the `entity_contains` method to filter entities based on the search term. The `entities` and `search` are strings.
"""

def entity_contains(entity, search):
    """
    Check if the entity contains the search term.
    """
    return search in entity

def search_entities(entities, search):
    """
    Iterate over entities from supplied iterator containing supplied search term.
    """
    for e in entities:
        if entity_contains(e, search):
            yield e