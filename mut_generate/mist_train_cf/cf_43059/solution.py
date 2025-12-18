"""
QUESTION:
Implement a function `validateInput(data, rules)` that takes two parameters: 
- `data`: a dictionary representing the input data to be validated, where the keys are the field names and the values are the input values.
- `rules`: a dictionary representing the validation rules, where the keys are the rule names and the values are the error messages with placeholders.

The function should iterate through the `rules` and validate the corresponding fields in the `data` dictionary. If any validation fails, the function should return a dictionary containing the field names as keys and the error messages as values. If all validations pass, the function should return an empty dictionary.
"""

def validateInput(data, rules):
    errors = {}
    for field, value in data.items():
        if field in rules:
            rule_message = rules[field]
            if 'string' in rule_message and not isinstance(value, str):
                errors[field] = rule_message.replace(':field:', field)
            elif 'numeric' in rule_message and not isinstance(value, (int, float)):
                errors[field] = rule_message.replace(':field:', field)
            elif 'date' in rule_message:
                try:
                    from datetime import datetime
                    datetime.strptime(value, '%Y-%m-%d')
                except ValueError:
                    errors[field] = rule_message.replace(':field:', field)
    return errors