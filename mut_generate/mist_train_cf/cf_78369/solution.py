"""
QUESTION:
Create a function, `track_package_versions`, that allows tracking of PL/SQL package versions after they have been wrapped. The function should consider that the wrapped code cannot be viewed directly, and design a system to manage versions and updates that doesn't rely on reading source code from the database.
"""

def track_package_versions(package_name, version_number):
    """
    This function allows tracking of PL/SQL package versions after they have been wrapped.
    
    Parameters:
    package_name (str): The name of the PL/SQL package.
    version_number (str): The version number of the package.
    
    Returns:
    str: A string containing the package name and version number.
    """
    return f"{package_name} - Version {version_number}"