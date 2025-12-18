"""
QUESTION:
Implement a function named `validate_boundary_pairs` that checks whether a given dictionary of boundary pairs is valid. The function should take a dictionary `pBd` as input and return `True` if the dictionary is valid, and `False` otherwise. The function should perform the following checks:
- `pBd` must be a dictionary.
- Each boundary pair in the dictionary must be unique.
- Each boundary pair must contain exactly one equals sign.
 
The boundary pair is unique if it is not present in the dictionary with the same names in either order, e.g., 'boundary1=boundary2' and 'boundary2=boundary1' are considered the same pair.
"""

def validate_boundary_pairs(pBd):
    if not isinstance(pBd, dict):
        return False

    bnPOOL = set()
    for pair in pBd:
        if '=' not in pair or pair.count('=') > 1:
            return False
        bn1, bn2 = pair.split('=')
        if (bn1, bn2) in bnPOOL or (bn2, bn1) in bnPOOL:
            return False
        bnPOOL.add((bn1, bn2))

    return True