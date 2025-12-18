"""
QUESTION:
You are given an integer K. Print the string obtained by repeating the string `ACL` K times and concatenating them.

For example, if K = 3, print `ACLACLACL`.

Constraints

* 1 \leq K \leq 5
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


K


Output

Print the string obtained by repeating the string `ACL` K times and concatenating them.

Example

Input

3


Output

ACLACLACL
"""

def generate_acl_string(K: int) -> str:
    """
    Generates a string by repeating the string "ACL" K times.

    Parameters:
    K (int): The number of times to repeat the string "ACL".

    Returns:
    str: The concatenated string of "ACL" repeated K times.
    """
    return 'ACL' * K