"""
QUESTION:
Implement a function `process_conditions` that takes a list of tuples representing database query conditions and returns a dictionary containing the processed conditions. The function should support the following operators: '=', '>', '<', '>=', '<=', '!='. If the operator is '=', the value should be directly assigned to the field in the dictionary. If the operator is '>', '<', '>=', or '<=', the value should be assigned to the field in the dictionary as a nested dictionary with the corresponding operator as the key. If the operator is '!=', the value should be assigned to the field in the dictionary as a nested dictionary with the key 'not_equal'. The function should handle each tuple in the input list as (field, operator, value).
"""

def process_conditions(conditions: list) -> dict:
    processed_conditions = {}
    for field, operator, value in conditions:
        if operator == '=':
            processed_conditions[field] = value
        elif operator in ['>', '<', '>=', '<=']:
            processed_conditions[field] = {operator: value}
        elif operator == '!=':
            processed_conditions[field] = {'not_equal': value}
    return processed_conditions