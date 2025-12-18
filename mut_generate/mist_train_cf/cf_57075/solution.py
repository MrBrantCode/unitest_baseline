"""
QUESTION:
In Delphi, a constant variable declared with the `const` keyword can be reassigned a value in older versions, but not in newer versions starting from Delphi 2009. Write a function called `is_delphi_const_reassignable` to check if a Delphi compiler version allows constant reassignment. The function should take a string representing the Delphi version as input and return True if the version allows constant reassignment and False otherwise. Assume that the version string can be 'Delphi 5', 'Delphi 2007', 'Delphi 2009', 'Delphi 2010', etc.
"""

def is_delphi_const_reassignable(delphi_version: str) -> bool:
    """
    Checks if a Delphi compiler version allows constant reassignment.

    Args:
        delphi_version (str): The Delphi version, e.g., 'Delphi 5', 'Delphi 2007', etc.

    Returns:
        bool: True if the version allows constant reassignment, False otherwise.
    """
    # Split the version string into parts
    version_parts = delphi_version.split()

    # Check if the version is in the 'Delphi X' format
    if len(version_parts) == 2 and version_parts[0] == 'Delphi':
        # Try to parse the version number
        try:
            version_number = int(version_parts[1])
        except ValueError:
            # If the version number is not an integer, return False
            return False

        # Versions before Delphi 2009 allow constant reassignment
        return version_number < 2009
    else:
        # If the version string is not in the 'Delphi X' format, return False
        return False