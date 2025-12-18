"""
QUESTION:
Create a function named `enforce_constraint_checking` that determines whether it's possible to enforce foreign key constraint checking in a database only when inserting new rows, while allowing the constraints to be violated when removing or updating rows.
"""

def enforce_constraint_checking(inserting: bool) -> bool:
    """
    Determines whether it's possible to enforce foreign key constraint checking in a database.
    
    Args:
    inserting (bool): A boolean indicating whether the operation is an insert (True) or not (False).
    
    Returns:
    bool: False, as it's not possible to enforce foreign key constraint checking only when inserting new rows.
    """
    return False