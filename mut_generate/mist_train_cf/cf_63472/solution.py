"""
QUESTION:
Write a function `modify_bool` that takes two boolean inputs, `bool1` and `bool2`. The function should return 'Yes' if `bool1` is True and `bool2` is False, 'No' if `bool1` is False and `bool2` is False, and 'Maybe' otherwise.
"""

def modify_bool(bool1, bool2): 
    if bool1 == True and bool2 == False:
        return 'Yes'
    elif bool1 == False and bool2 == False: 
        return 'No'
    else:
        return 'Maybe'