"""
QUESTION:
Implement a function named "compare" to mimic the behavior of operator overloading for equality comparison in ActionScript, which does not natively support operator overloading.
"""

def compare(obj1, obj2):
    """
    Deep comparison function to compare two objects.

    Args:
        obj1 (object): The first object to compare.
        obj2 (object): The second object to compare.

    Returns:
        bool: True if the objects are equal, False otherwise.
    """
    # If both objects are dictionaries
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        # Compare the items in the dictionaries
        return obj1 == obj2

    # If both objects are lists or tuples
    elif isinstance(obj1, (list, tuple)) and isinstance(obj2, (list, tuple)):
        # Compare the elements in the lists or tuples
        if len(obj1) != len(obj2):
            return False
        for elem1, elem2 in zip(obj1, obj2):
            if not compare(elem1, elem2):
                return False
        return True

    # If the objects are of different types or not comparable
    else:
        # Try to compare the objects directly
        try:
            return obj1 == obj2
        except Exception:
            # If the comparison fails, return False
            return False