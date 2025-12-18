"""
QUESTION:
Implement a function `check_bet` that takes in the following parameters: `isAdmin`, `adminUnlim`, `reserveXP`, and `minRole`, as well as `author_top_role_name`. The function should return two boolean values: `approve` and `decrement`, based on the following rules:
- If `isAdmin` is True and `adminUnlim` is True, `approve` is True and `decrement` is False.
- If `reserveXP` is greater than 0, `approve` is True and `decrement` is False.
- If `author_top_role_name` is greater than or equal to `minRole`, `approve` is True and `decrement` is True.
- If none of the above conditions are met, `approve` is False and `decrement` is True.
"""

def check_bet(isAdmin, adminUnlim, reserveXP, minRole, author_top_role_name):
    if isAdmin and adminUnlim:
        return True, False
    elif reserveXP > 0:
        return True, False
    elif author_top_role_name >= minRole:
        return True, True
    else:
        return False, True