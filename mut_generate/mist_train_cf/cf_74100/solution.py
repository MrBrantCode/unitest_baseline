"""
QUESTION:
Develop a function named `compute_depreciation` that calculates the depreciated value of an asset using either the straight-line or declining balance method. The function should take in the initial cost of the asset, its salvage value at the end of its useful life, the total years of its useful life, and the annual depreciation rate for the declining balance method (optional). It should return the annual depreciation value. If the declining balance method is used, the annual depreciation rate is required. The function should also include error handling to check for invalid parameters such as negative initial cost, zero or negative years of useful life, and invalid annual depreciation rates.
"""

def compute_depreciation(initial_cost, salvage_value, useful_life_years, annual_depreciation_rate = None, method='straight-line'):
    # handle invalid input errors
    if initial_cost < 0:
        return "Error: Initial cost cannot be negative."
    elif useful_life_years <= 0:
        return "Error: Useful life years cannot be zero or negative."
    elif salvage_value < 0:
        return "Error: Salvage value cannot be negative."
    elif method == 'declining-balance' and (annual_depreciation_rate is None or annual_depreciation_rate <= 0 or annual_depreciation_rate > 1):
        return "Error: Invalid annual depreciation rate. It should be a positive decimal value not exceeding 1."

    # straight-line method
    if method == 'straight-line':
        annual_depreciation = (initial_cost - salvage_value) / useful_life_years
        return annual_depreciation

    # declining balance method
    else:
        annual_depreciation = initial_cost * annual_depreciation_rate
        return annual_depreciation