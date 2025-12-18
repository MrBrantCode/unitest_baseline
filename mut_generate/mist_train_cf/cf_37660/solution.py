"""
QUESTION:
Implement a function `validate_parameters` that takes two dictionaries as input: `signature` and `parameters`. The `signature` dictionary contains parameter names as keys and expected types as values. The expected types are represented by the strings '<boolean>', '<enum>', and '<arbitrary-obj>'. The function should return True if the parameters match the signature and False otherwise.

The function should check if each parameter in the signature exists in the parameters dictionary and if its type matches the expected type. The function should also validate the type of '<enum>' to be one of 'option1', 'option2', 'option3' and '<arbitrary-obj>' to be a dictionary.

CONSTANTS: BOOLEAN_TYPE = '<boolean>', ENUM_TYPE = '<enum>', ARBITRARY_OBJ_TYPE = '<arbitrary-obj>'
"""

BOOLEAN_TYPE = '<boolean>'
ENUM_TYPE = '<enum>'
ARBITRARY_OBJ_TYPE = '<arbitrary-obj>'

def validate_parameters(signature: dict, parameters: dict) -> bool:
    for param, expected_type in signature.items():
        if param not in parameters:
            return False  
        if expected_type == BOOLEAN_TYPE:
            if not isinstance(parameters[param], bool):
                return False
        elif expected_type == ENUM_TYPE:
            if parameters[param] not in ['option1', 'option2', 'option3']:
                return False
        elif expected_type == ARBITRARY_OBJ_TYPE:
            if not isinstance(parameters[param], dict):
                return False
        else:
            return False  
    return True