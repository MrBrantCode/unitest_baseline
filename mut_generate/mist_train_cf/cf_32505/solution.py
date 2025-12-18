"""
QUESTION:
Implement the `Items` class with an `__init__` method that takes `date_range`, `type_group`, `order_by`, and `num_items` as parameters. The class should have a `write_statement` method that constructs and returns an SQL statement based on the provided parameters. The `date_range` is a tuple of two dates or "All" for no date filter, `type_group` is either "All" or a specific type, `order_by` is either "Latest" or "Oldest", and `num_items` is the number of items to retrieve. If `date_range` or `type_group` is "All", do not include them in the SQL statement's WHERE clause. Sort the results by date in the specified order and limit the results to `num_items`.
"""

def entrance(date_range, type_group, order_by, num_items):
    sql_statement = "SELECT * FROM items"
    conditions = []
    
    if date_range != "All":
        conditions.append(f"date BETWEEN '{date_range[0]}' AND '{date_range[1]}'")
    if type_group != "All":
        conditions.append(f"type = '{type_group}'")
        
    if conditions:
        sql_statement += " WHERE " + " AND ".join(conditions)
    
    if order_by == "Latest":
        order = "DESC"
    elif order_by == "Oldest":
        order = "ASC"
    
    sql_statement += f" ORDER BY date {order} LIMIT {num_items};"
    
    return sql_statement