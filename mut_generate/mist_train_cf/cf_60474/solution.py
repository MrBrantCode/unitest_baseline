"""
QUESTION:
Implement the `create_keyspace` function that creates a keyspace in Cassandra with a specified name and replication factor. The function should return the CQL command to create the keyspace. The replication factor should default to 3 if not provided.
"""

def create_keyspace(keyspace_name, replication_factor=3):
    """
    Creates a keyspace in Cassandra with a specified name and replication factor.
    
    Args:
    keyspace_name (str): The name of the keyspace to be created.
    replication_factor (int, optional): The replication factor for the keyspace. Defaults to 3.
    
    Returns:
    str: The CQL command to create the keyspace.
    """
    cql_command = f"CREATE KEYSPACE {keyspace_name} WITH REPLICATION = {{'class' : 'SimpleStrategy', 'replication_factor' : {replication_factor}}};"
    return cql_command