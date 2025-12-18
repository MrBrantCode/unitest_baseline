"""
QUESTION:
Create a function called `process_connection_info` that takes a dictionary as input. The dictionary contains 'user' and 'pass' as keys with string values representing the username and password for a database connection. The function should modify the input dictionary by adding 'host', 'port', and 'connection_timeout' with values 'test-host', 5433, and 5 respectively, and rename 'pass' to 'password'. The function should then return the modified dictionary.
"""

def process_connection_info(connection_info):
    """
    Modify the input dictionary to include 'host', 'port', and 'connection_timeout' 
    with values 'test-host', 5433, and 5 respectively, and rename 'pass' to 'password'.

    Args:
        connection_info (dict): A dictionary containing 'user' and 'pass' as keys.

    Returns:
        dict: The modified dictionary with added and renamed keys.
    """
    connection_info['host'] = 'test-host'
    connection_info['port'] = 5433
    connection_info['connection_timeout'] = 5
    connection_info['password'] = connection_info.pop('pass')
    return connection_info