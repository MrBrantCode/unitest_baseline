"""
QUESTION:
Write a function `generateInsertQuery` that takes a string representing a SELECT query and a target table name as input, and returns a string representing the corresponding INSERT query. The SELECT query will always be in the format `SELECT column1, column2, ... FROM table_name WHERE condition;` and the generated INSERT query should insert the selected columns' values into the specified target table. The input SELECT query and target table name are guaranteed to be well-formed and valid.
"""

def generateInsertQuery(select_query: str, target_table: str) -> str:
    # Extracting the columns from the SELECT query
    columns_start_index = select_query.find('SELECT') + len('SELECT')
    columns_end_index = select_query.find('FROM')
    columns = select_query[columns_start_index:columns_end_index].strip()

    # Constructing the INSERT query
    insert_query = f"INSERT INTO {target_table} ({columns}) {select_query}"

    return insert_query