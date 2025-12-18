"""
QUESTION:
Create a function `limit_presto_concurrent_queries` that limits the maximum number of concurrent queries per user in Apache Presto. The function should consider that Apache Presto does not inherently support this feature, and the solution should provide a workaround. The function should not require the management console to limit the maximum number of concurrent queries per logged-in user.
"""

def limit_presto_concurrent_queries(user, max_concurrent_queries):
    """
    Limits the maximum number of concurrent queries per user in Apache Presto.
    
    This function uses a simple dictionary to store the current number of queries per user.
    It is a basic implementation and may need to be adapted to your specific use case.
    
    Parameters:
    user (str): The username to limit the queries for
    max_concurrent_queries (int): The maximum number of concurrent queries allowed
    
    Returns:
    bool: True if the query can be executed, False if the limit is reached
    """

    # Initialize a dictionary to store the current number of queries per user
    concurrent_queries = {}

    # Check if the user has already reached the limit
    if user in concurrent_queries and concurrent_queries[user] >= max_concurrent_queries:
        return False

    # If the user is not in the dictionary, add them with a count of 1
    if user not in concurrent_queries:
        concurrent_queries[user] = 1
    else:
        # If the user is already in the dictionary, increment their count
        concurrent_queries[user] += 1

    return True