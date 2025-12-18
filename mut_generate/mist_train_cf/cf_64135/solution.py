"""
QUESTION:
Write a function `refactor_class_names` that renames specific class names in Python and XML code without renaming them in other class names. The function should be able to rename `AdminAction` to `AdminActionPlug` and `AdminActionLogger` to `AdminActionLoggerPlug` without incorrectly renaming `AdminAction` in `AdminActionLogger`.
"""

import re

def refactor_class_names(code):
    """
    Refactor specific class names in Python and XML code.

    Args:
    code (str): The Python or XML code to refactor.

    Returns:
    str: The refactored code.
    """

    # Refactor AdminAction to AdminActionPlug
    code = re.sub(r'\bAdminAction\b', 'AdminActionPlug', code)
    
    # Refactor AdminActionLogger to AdminActionLoggerPlug
    code = re.sub(r'\bAdminActionLogger\b', 'AdminActionLoggerPlug', code)

    return code