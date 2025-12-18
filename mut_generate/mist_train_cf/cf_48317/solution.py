"""
QUESTION:
Rank the given time complexities from slowest to fastest growth rate: O(N), O(N^(1/2)), O(N^(1/4)), and O(N^(1/N)). Assume N is a large input size and provide the correct order without justification or explanation.
"""

import numpy as np

def time_complexity_growth_rates(N):
    return N**(1/N), N**(1/4), N**(1/2), N

# Returns growth rates in order from slowest to fastest: O(N^(1/N)), O(N^(1/4)), O(N^(1/2)), O(N)