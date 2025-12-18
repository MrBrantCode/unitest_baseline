"""
QUESTION:
Implement a `switch_case` function in Python that takes a `case_value` as input and returns the corresponding case value from a predefined set of cases. The function should have a default case to handle unknown `case_value`. Use dictionary mapping to achieve this functionality and include error handling to ensure the program doesn't crash when an unexpected `case_value` is encountered. The function should be able to handle cases where `case_value` is not found in the predefined set of cases.
"""

def switch_case(case_value):
    """
    This function acts like a switch-case structure in Python.
    
    It takes a case_value as input and returns the corresponding case value 
    from a predefined set of cases. The function has a default case to handle 
    unknown case_value. It uses dictionary mapping to achieve this functionality 
    and includes error handling to ensure the program doesn't crash when an 
    unexpected case_value is encountered.

    Args:
    case_value: The value to be matched in the switch-case structure.

    Returns:
    The corresponding case value if found, otherwise the default case value.
    """
    
    # Define the cases in a dictionary
    switcher = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3",
        'default': "Default Case"
    }
    
    # Use get method to return the corresponding case value if found, 
    # otherwise return the default case value
    return switcher.get(case_value, switcher['default'])