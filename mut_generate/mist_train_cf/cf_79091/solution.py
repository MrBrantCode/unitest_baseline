"""
QUESTION:
Convert the PostgreSQL query "SELECT * FROM products WHERE quantity > 50 AND price < 200 ORDER BY price ASC" into its equivalent Cassandra Query Language (CQL) statement, considering the restrictions and limitations of CQL, particularly with regards to sorting and filtering on non-primary key columns.
"""

def postgres_to_cql(postgres_query):
    """
    A simple function to convert a PostgreSQL query to its equivalent Cassandra Query Language (CQL) statement.

    Args:
        postgres_query (str): The PostgreSQL query to be converted.

    Returns:
        str: The equivalent CQL query.
    """
    # Assuming the PostgreSQL query is in the format "SELECT * FROM table_name WHERE conditions ORDER BY column_name ASC"
    # This function does not handle all possible PostgreSQL queries and is for demonstration purposes only
    query_parts = postgres_query.split("WHERE")
    table_name = query_parts[0].split("FROM")[1].strip()
    conditions = query_parts[1].split("ORDER BY")[0].strip()
    order_by_column = query_parts[1].split("ORDER BY")[1].split("ASC")[0].strip()

    # Cassandra requires the ordering column to be a clustering column (part of the compound primary key)
    # This example assumes the table schema is already defined with the correct primary key
    cql_query = f"SELECT * FROM {table_name} WHERE {conditions} AND {order_by_column} < ? ALLOW FILTERING;"

    return cql_query

# Note that this function does not actually convert the PostgreSQL query to CQL but rather generates a CQL query 
# based on the provided PostgreSQL query. The generated CQL query may not be semantically equivalent to the 
# original PostgreSQL query due to the limitations of CQL.