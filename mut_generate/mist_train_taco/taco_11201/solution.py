"""
QUESTION:
Correct this code so that it takes one argument, `x`, and returns "`x` is more than zero" if `x` is positive (and nonzero), and otherwise, returns "`x` is equal to or less than zero." In both cases, replace `x` with the actual value of `x`.
"""

def check_number_status(x):
    if x > 0:
        return f"{x} is more than zero."
    else:
        return f"{x} is equal to or less than zero."