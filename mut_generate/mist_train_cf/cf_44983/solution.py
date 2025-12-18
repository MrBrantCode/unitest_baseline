"""
QUESTION:
Write a function named 'compatible_django_version' that determines the Django version compatible with a given Python version, assuming Django dropped support for Python 3.4 in version 2.0 and f-string formatting was introduced in Python 3.6. The function should take the Python version as a string in the format 'X.X' and return the latest Django version that supports that Python version.
"""

def compatible_django_version(python_version):
    """
    This function determines the Django version compatible with a given Python version.
    
    Parameters:
    python_version (str): The Python version as a string in the format 'X.X'
    
    Returns:
    str: The latest Django version that supports the given Python version.
    """
    
    # Split the Python version into major and minor version numbers
    major, minor = map(int, python_version.split('.'))
    
    # Django dropped support for Python 3.4 in version 2.0
    if (major, minor) < (3, 5):
        return '1.11'
    
    # f-string formatting was introduced in Python 3.6
    elif (major, minor) < (3, 6):
        return '2.0'
    
    # For Python 3.6 and above, the latest Django version is 3.2
    else:
        return '3.2'