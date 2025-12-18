"""
QUESTION:
Create a function `assertAllResponsesHaveBlankField` that takes in a dictionary `criteria`, a list of attribute names `attributes`, and a lambda function `check_function`. The function should return `True` if all credits have blank fields for the specified attributes based on the provided criteria, and `False` otherwise. The `criteria` dictionary contains attribute names suffixed with '__isblank' as keys and string representations of boolean values as values. The `check_function` takes a credit object as input and returns a boolean value based on the attribute's blank field. Assume that a list of credits is accessible within the function.
"""

def assertAllResponsesHaveBlankField(criteria, attributes, check_function):
    for attribute in attributes:
        if attribute in criteria and criteria[attribute + '__isblank'].lower() == 'true':
            for credit in credits:
                if not check_function(credit):
                    return False
    return True