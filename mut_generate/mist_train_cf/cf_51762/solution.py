"""
QUESTION:
Given an exception code, write a function named `lookup_exception` that takes the exception code as input and returns information about the actual exception that was thrown. The function should assume that the exception code may not be a standard Windows exception code and provide alternatives to investigate further.
"""

def lookup_exception(exception_code):
    """
    This function takes an exception code as input and returns information about the actual exception that was thrown.
    If the exception code is not a standard Windows exception code, it provides alternatives to investigate further.

    Parameters:
    exception_code (int): The exception code to be looked up.

    Returns:
    str: Information about the exception code.
    """

    # Check if the exception code is a standard Windows exception code
    if exception_code & 0xFF000000 == 0xC0000000 or exception_code & 0xFF000000 == 0xE0000000:
        # If it is, return the corresponding exception information
        return "Standard Windows exception code"
    else:
        # If not, provide alternatives to investigate further
        return """The exception code doesn't appear to be a standard Windows exception code. 
                  You can try checking the application logs, contacting the vendor for help, 
                  or checking the dump file for other exception codes."""