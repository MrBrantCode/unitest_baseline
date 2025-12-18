"""
QUESTION:
Create a function called `lives` that takes two parameters: `elephant` and `place`. The function should return `True` if an elephant lives in the given place according to the statement "An elephant only lives in an African safari." The function should return `True` if `place` is 'African safari' regardless of the value of `elephant`, and `False` otherwise if `place` is not 'African safari' and `elephant` is `True`. If `elephant` is `False`, the function should return `True` for any `place`.
"""

def lives(elephant, place):
    if place != 'African safari':
        return elephant == False
    else:
        return True