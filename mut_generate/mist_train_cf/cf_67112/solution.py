"""
QUESTION:
Write a function `filter_table` that takes a table (a list of lists), a list of column names `cols`, and a predicate function as input. The function should parse the table data to correctly identify numeric values, filter the table rows based on the predicate function, and return a new table containing only the specified columns. The returned table should include the column headers. The predicate function should compare values within each row and return a boolean value.
"""

def filter_table(table, cols, predicate):
    headers = table[0]
    data = table[1:]

    # Parsing numeric value
    for row in data:
        for i in range(len(row)):
            if row[i].isdigit():
                row[i] = int(row[i])

    # Filtering and selecting columns
    filtered_table = [[row[headers.index(col)] for col in cols if col in headers] for row in data if predicate(row)]

    # Including headers back
    filtered_table.insert(0, [col for col in headers if col in cols])
    return filtered_table