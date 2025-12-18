"""
QUESTION:
Write a function `get_foreign_keys` that takes a Django model as input and returns a list of tuples, where each tuple contains a foreign key field and its corresponding related model. The function should only consider explicit `ForeignKey` fields defined on the model and exclude implicit related fields.
"""

def get_foreign_keys(model):
    """
    Returns a list of tuples, where each tuple contains a foreign key field and its corresponding related model.

    Args:
        model (Django model): The model to extract foreign keys from.

    Returns:
        list[tuple]: A list of tuples containing foreign key fields and their related models.
    """
    foreign_keys = []
    for field in model._meta.get_fields(include_parents=False):
        if field.is_relation and field.many_to_one:
            foreign_keys.append((field, field.related_model))
    return foreign_keys