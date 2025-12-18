"""
QUESTION:
Implement a function `mock_framework_selection` that returns the best mock object framework for creating mock objects in Java based on given conditions. The function should take two parameters: `has_static_methods` and `is_large_scale`. The function should return the name of the best framework.
"""

def mock_framework_selection(has_static_methods, is_large_scale):
    """
    Returns the best mock object framework for creating mock objects in Java.

    Parameters:
    has_static_methods (bool): Whether the application uses static methods.
    is_large_scale (bool): Whether the application is large scale.

    Returns:
    str: The name of the best framework.
    """
    if has_static_methods:
        if is_large_scale:
            return "PowerMock with Mockito"
        else:
            return "PowerMock"
    else:
        return "Mockito"