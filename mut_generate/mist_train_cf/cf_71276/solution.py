"""
QUESTION:
Write a function named `check_variables` that takes two variables VAR1 and VAR2 as input. If either VAR1 or VAR2 is null or undefined, the function should return an empty string. Otherwise, it should return the value of VAR2. The function should not take any other parameters besides VAR1 and VAR2.
"""

def check_variables(VAR1, VAR2):
    if VAR1 is None or VAR2 is None:
        return ""
    return VAR2