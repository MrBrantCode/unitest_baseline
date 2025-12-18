"""
QUESTION:
Create a function `compare_and_modify_sum` that takes two non-negative integers as input, checks whether they are odd or even, compares them to determine their relationship, calculates their sum, and modifies the sum by adding 2 if it's odd or subtracting 2 if it's even. The function should then return a string describing the findings.
"""

def compare_and_modify_sum(var1, var2):
    """
    This function compares two non-negative integers, determines their relationship,
    calculates their sum, and modifies the sum based on whether it's odd or even.

    Args:
    var1 (int): The first non-negative integer.
    var2 (int): The second non-negative integer.

    Returns:
    str: A string describing the findings.
    """

    # Checking if the numbers are odd or even
    var1_type = "odd" if var1 % 2 == 1 else "even"
    var2_type = "odd" if var2 % 2 == 1 else "even"

    # Checking the relationship between the two numbers
    if var1 == var2:
        relationship = "equal to"
    elif var1 < var2:
        relationship = "<"
    else:
        relationship = ">"

    # Checking sum is odd or even
    sum_var = var1 + var2
    sum_type = "odd" if sum_var % 2 == 1 else "even"

    # Modifying the sum
    if sum_type == "odd":
        sum_var += 2
    else:
        sum_var -= 2

    # Reporting the findings
    return "Variable1 is {0} and Variable2 is {1}. Variable1 {2} Variable2 and sum after modification: {3}.".format(var1_type, var2_type, relationship, sum_var)