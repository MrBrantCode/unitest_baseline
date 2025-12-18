"""
QUESTION:
Create a function named check_condition that takes four integer parameters a, b, c, and d, and returns a string value based on the following conditions:
- If a is divisible by b, return "Yes".
- If a and b are both divisible by c, return "Maybe".
- If d is divisible by c, return "Certainly".
- If none of the above conditions are met, return "No".
"""

def check_condition(a, b, c, d):
    """
    This function checks the divisibility conditions of the given integers a, b, c, and d.

    Args:
        a (int): The first integer.
        b (int): The second integer.
        c (int): The third integer.
        d (int): The fourth integer.

    Returns:
        str: A string indicating whether the conditions are met.
    """
    if a % b == 0:
        return "Yes"
    elif a % c == 0 and b % c == 0:
        return "Maybe"
    elif d % c == 0:
        return "Certainly"
    else:
        return "No"