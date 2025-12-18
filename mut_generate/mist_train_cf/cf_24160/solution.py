"""
QUESTION:
Write a function `error_severity` that determines the severity of an error based on its error code and message. The function should take two parameters: `error_code` (an integer) and `error_message` (a string). The function should return a string representing the severity level of the error, which can be 'low', 'medium', or 'high'. Assume that higher error codes correspond to higher severity levels and more detailed error messages indicate higher severity levels.
"""

def error_severity(error_code, error_message):
    """
    Determine the severity of an error based on its error code and message.

    Parameters:
    error_code (int): The code of the error.
    error_message (str): The message of the error.

    Returns:
    str: The severity level of the error ('low', 'medium', or 'high').
    """
    
    # Define the threshold for high error codes
    high_error_code_threshold = 1000
    
    # Define keywords for high severity error messages
    high_severity_keywords = ['system', 'application', 'critical', 'fatal']
    
    # Check if the error code is high
    if error_code >= high_error_code_threshold:
        return 'high'
    
    # Check if the error message contains any high severity keywords
    if any(keyword in error_message.lower() for keyword in high_severity_keywords):
        return 'high'
    
    # If the error code is not high and the message does not contain any high severity keywords,
    # determine the severity based on the length of the error message
    if len(error_message) > 50:
        return 'medium'
    else:
        return 'low'