"""
QUESTION:
Create a function `multi_column_sort` that takes `columns`, `order`, `limit`, and `start` as parameters. The function should generate a SQL query that sorts a table by multiple columns based on the provided `order` parameter. If `order` is not provided, it should default to `"bukti_transfer.tgl_transfer DESC, bukti_transfer.nama_usaha ASC"`. The `order` parameter is an array of objects where each object contains a `column` index and a `dir` direction (`asc` or `desc`). The function should return the generated SQL query. The SQL query should also include a LIMIT clause with the provided `limit` and an OFFSET clause with the provided `start`. Note: The function should use parameterized queries or prepared statements to prevent SQL injection attacks.
"""

def multi_column_sort(columns, order=None, limit=None, start=0):
    """
    Generate a SQL query that sorts a table by multiple columns based on the provided order parameter.

    Args:
        columns (list): A list of column names.
        order (list, optional): A list of objects where each object contains a column index and a direction. Defaults to None.
        limit (int, optional): The number of rows to return. Defaults to None.
        start (int, optional): The starting row. Defaults to 0.

    Returns:
        str: The generated SQL query.
    """
    if order is None:
        order = [{"column": "bukti_transfer.tgl_transfer", "dir": "DESC"}, {"column": "bukti_transfer.nama_usaha", "dir": "ASC"}]
    
    order_parts = []
    for o in order:
        column = columns[o['column']] if isinstance(o['column'], int) else o['column']
        dir = o['dir']
        order_parts.append(f"{column} {dir}")
    
    order_str = ", ".join(order_parts)
    
    query = f"SELECT * FROM my_table ORDER BY {order_str}"
    
    if limit is not None:
        query += f" LIMIT {limit}"
    
    if start > 0:
        query += f" OFFSET {start}"
    
    return query