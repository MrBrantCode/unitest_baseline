"""
QUESTION:
Assign a value to `name` based on a complex condition involving at least 5 variables and 3 logical operators. The condition should include both logical and comparison operators, be nested within multiple if-else statements with at least 4 levels of nesting, and have a time complexity of at least O(n^2), where n is the number of variables involved in the condition.
"""

def assign_name(variable1, variable2, variable3, variable4, variable5):
    if variable1 > variable2:
        if variable3 <= variable4 and variable5 != 0:
            name = "John"
        elif variable4 < variable5 or variable2 == variable3:
            name = "Jane"
        else:
            name = "Unknown"
    else:
        if variable1 >= variable4 and variable2 < variable5:
            if variable3 > variable5 or variable4 == 0:
                name = "Alice"
            else:
                name = "Bob"
        else:
            name = "Unknown"
    return name