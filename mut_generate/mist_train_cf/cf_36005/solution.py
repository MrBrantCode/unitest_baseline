"""
QUESTION:
Implement a function `convert_to_sql_types(data_types)` that takes a dictionary `data_types` as input and returns a new dictionary with the data types converted to their SQL equivalents. The function should use the following mapping: "int" to "integer", "float" to "real", "string" to "varchar", and "timestamp" to "timestamp". If a data type is not found in the mapping, it should be left unchanged in the output dictionary.
"""

def convert_to_sql_types(data_types):
    sql_mapping = {
        "int": "integer",
        "float": "real",
        "string": "varchar",
        "timestamp": "timestamp"
    }
    converted_types = {}
    for key, value in data_types.items():
        if value in sql_mapping:
            converted_types[key] = sql_mapping[value]
        else:
            converted_types[key] = value
    return converted_types