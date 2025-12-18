"""
QUESTION:
Write a function `extract_sql_info(sql_template)` that takes a SQL template string as input and returns a dictionary containing the extracted information. The function should extract the selected columns, table names, and conditions used in the WHERE clause. The SQL template string follows the format: "SELECT ... FROM ... WHERE ...".

The extracted information should be returned in the following dictionary format:
- "selected_columns": a list of selected columns
- "table_names": a list of table names
- "where_conditions": the conditions used in the WHERE clause as a string.

The function should assume that the SQL template string is well-formed and follows the specified format.
"""

import re

def extract_sql_info(sql_template):
    selected_columns = re.findall(r'Select (.*?) FROM', sql_template, re.IGNORECASE)[0].split(', ')
    table_names = re.findall(r'FROM (.*?) WHERE', sql_template, re.IGNORECASE)[0].split(', ')
    where_conditions = re.findall(r'WHERE (.*)', sql_template, re.IGNORECASE)[0]

    return {
        "selected_columns": selected_columns,
        "table_names": table_names,
        "where_conditions": where_conditions
    }