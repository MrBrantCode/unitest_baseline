"""
QUESTION:
Create a function `contest_brackets(n, offset=1)` that generates the final contest matches string for the NBA playoffs. The function takes the number of teams `n` as input, where `n` is a positive integer within the range [2, 212] and can be converted into the form 2k, where k is a positive integer. The function should return a string representing the final contest matches, using parentheses for pairing and commas for partition, such that a stronger team is paired with a weaker one.
"""

def contest_brackets(n, offset=1):
    if n == 2:
        return "(" + str(offset) + "," + str(offset+1) + ")"
    else:
        return "(" + contest_brackets(n//2, offset) + "," + contest_brackets(n//2, offset+n//2) + ")"