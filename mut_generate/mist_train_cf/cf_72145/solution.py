"""
QUESTION:
Implement a validation framework that can be used independently and integrated into Spring MVC flow, applicable to both web requests and web-service calls. The framework should be reusable, extensible, and decoupled from Spring's Validator interface. Design a validation strategy that can accommodate complex validation needs, including data binding and manual validation.
"""

def entrance(data):
    """
    This function serves as the central validation service, 
    taking in data to be validated and returning the result.

    Args:
    data (dict): The data to be validated.

    Returns:
    bool: True if the data is valid, False otherwise.
    """

    # Implement your validation logic here
    # For example, you can use a dictionary to store validation rules
    validation_rules = {
        'key1': lambda x: isinstance(x, str),
        'key2': lambda x: isinstance(x, int)
    }

    for key, rule in validation_rules.items():
        if key not in data or not rule(data[key]):
            return False

    return True