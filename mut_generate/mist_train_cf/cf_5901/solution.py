"""
QUESTION:
Write a function `assign_name` that takes six variables as input and assigns a value to `name` based on a complex condition involving at least 5 variables and 3 logical operators. The condition should include both logical and comparison operators, and at least 2 bitwise operators. The condition should be nested within at least 5 levels of if-else statements, and its complexity should be at least O(n^3), where n is the number of variables involved in the condition.
"""

def assign_name(var1, var2, var3, var4, var5, var6):
    """
    Assign a value to 'name' based on a complex condition involving six variables.

    Args:
        var1 (int): The first variable.
        var2 (int): The second variable.
        var3 (int): The third variable.
        var4 (int): The fourth variable.
        var5 (int): The fifth variable.
        var6 (int): The sixth variable.

    Returns:
        str: The assigned name.
    """
    if var1 > var2:
        if var3 <= var4:
            if var5 & var6:
                if (var1 + var3) == (var2 - var4):
                    if (var5 | var6) and (var1 * var2 > var3):
                        return "Condition met"
                    else:
                        return "Inner condition not met"
                else:
                    return "Inner condition not met"
            else:
                return "Inner condition not met"
        else:
            return "Inner condition not met"
    else:
        return "Outer condition not met"