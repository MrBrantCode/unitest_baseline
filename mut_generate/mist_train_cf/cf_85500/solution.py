"""
QUESTION:
Design a function named `transform_data` that takes a dataset and a list of transformation rules as input. The dataset is a list of dictionaries, where each dictionary represents a record. The transformation rules are tuples of the form (action, column, value), where 'action' can be one of the following: 'add', 'subtract', 'multiply', 'divide', 'replace', or 'delete'. The function should apply the transformation rules to the dataset and return the transformed dataset.

The function should support the following actions:
- 'add': adds the value to the specified column.
- 'subtract': subtracts the value from the specified column.
- 'multiply': multiplies the value with the specified column.
- 'divide': divides the specified column by the value.
- 'replace': replaces the values in the specified column based on a dictionary of replacements.
- 'delete': deletes the specified column.

Note that the dataset and transformation rules are the only inputs to the function.
"""

def transform_data(data, rules):
    # Iterate through each rule
    for rule in rules:
        action, column, value = rule
        
        for record in data:
            if column in record:
                if action == "add":
                    record[column] += value
                elif action == "subtract":
                    record[column] -= value
                elif action == "multiply":
                    record[column] *= value
                elif action == "divide":
                    record[column] /= value
                elif action == "replace":
                    if record[column] in value:
                        record[column] = value[record[column]]
                elif action == "delete":
                    del record[column]
    return data