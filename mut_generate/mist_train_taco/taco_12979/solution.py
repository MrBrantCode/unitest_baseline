"""
QUESTION:
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
 
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

 
Constraints:

The given address is a valid IPv4 address.
"""

def defang_ip_address(address: str) -> str:
    """
    Converts a given valid IPv4 address into its defanged version by replacing each period "." with "[.]".

    Parameters:
    address (str): The input IPv4 address.

    Returns:
    str: The defanged version of the input IP address.
    """
    return address.replace('.', '[.]')