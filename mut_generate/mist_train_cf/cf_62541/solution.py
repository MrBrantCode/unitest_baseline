"""
QUESTION:
Write a function `classify_ip(ip)` that categorizes a private IP address into its respective class (A, B, C) based on the private IP ranges. The function should return the class of the IP address, or "Not a private IP" if it does not match any of the private IP ranges.
"""

import re

def classify_ip(ip):
    """
    Classify a private IP address into its respective class (A, B, C) based on the private IP ranges.
    
    Args:
        ip (str): The IP address to classify.
    
    Returns:
        str: The class of the IP address, or "Not a private IP" if it does not match any of the private IP ranges.
    """

    # Define regular expression patterns for each class
    patternA = r"^10\.([01]?\d?\d|2[0-4]\d|25[0-5])\.([01]?\d?\d|2[0-4]\d|25[0-5])\.([01]?\d?\d|2[0-4]\d|25[0-5])$"
    patternB = r"^172\.(1[6-9]|2\d|3[01])\.([01]?\d?\d|2[0-4]\d|25[0-5])\.([01]?\d?\d|2[0-4]\d|25[0-5])$"
    patternC = r"^192\.168\.([01]?\d?\d|2[0-4]\d|25[0-5])\.([01]?\d?\d|2[0-4]\d|25[0-5])$"

    # Check if the IP matches any of the patterns
    if re.match(patternA, ip):
        return "Class A"
    elif re.match(patternB, ip):
        return "Class B"
    elif re.match(patternC, ip):
        return "Class C"
    else:
        return "Not a private IP"