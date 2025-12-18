"""
QUESTION:
Write a function `validate_spill(spill: str) -> bool` that checks if a given string `spill` representing a spill of parameters and their values is well-formed. The string is formatted as an integer `n_par` followed by `n_par` parameter names and then `n_par`^2 parameter values, all separated by commas. The function should return `True` if the number of elements in the spill matches the expected count based on the number of parameters (1 + `n_par` + `n_par`^2), and `False` otherwise.
"""

def validate_spill(spill: str) -> bool:
    spill_sep = spill.split(',')
    n_par = int(spill_sep[0])
    expected_count = 1 + n_par + n_par**2
    return len(spill_sep) == expected_count