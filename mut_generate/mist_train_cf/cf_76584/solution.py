"""
QUESTION:
Write a function called `should_use_table_clusters` with a boolean return type. The function should take two parameters: `is_read_heavy` and `has_predictable_access_patterns`, both of which are booleans. Return True if using table clusters is recommended and False otherwise. Assume that the database is not write-heavy and storage is not a concern.
"""

def should_use_table_clusters(is_read_heavy, has_predictable_access_patterns):
    """
    Recommends whether to use table clusters based on the given parameters.

    Args:
    is_read_heavy (bool): Whether the database is read-heavy.
    has_predictable_access_patterns (bool): Whether the database has predictable data access patterns.

    Returns:
    bool: True if using table clusters is recommended, False otherwise.
    """
    return is_read_heavy and has_predictable_access_patterns