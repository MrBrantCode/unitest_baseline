"""
QUESTION:
Write a function `create_keyspace` that creates a keyspace in Apache Cassandra NoSQL database using the Cassandra Query Language (CQL) with a specified replication factor. The function should take two parameters: `keyspace_name` and `replication_factor`. The function should return a CQL command string. The keyspace should use the 'SimpleStrategy' class for replication.
"""

def create_keyspace(keyspace_name, replication_factor):
    """
    Creates a keyspace in Apache Cassandra NoSQL database using the Cassandra Query Language (CQL) with a specified replication factor.
    
    Parameters:
    keyspace_name (str): The name of the keyspace to be created.
    replication_factor (int): The replication factor for the keyspace.
    
    Returns:
    str: A CQL command string to create the keyspace.
    """
    return f"CREATE KEYSPACE {keyspace_name} WITH REPLICATION = {{ 'class' : 'SimpleStrategy', 'replication_factor' : {replication_factor} }};"