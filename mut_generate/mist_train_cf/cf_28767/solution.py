"""
QUESTION:
Implement a function `calculate_efficiency(n, sheffc, bfeffc)` that calculates the efficiency for the "bo" algorithm and compiles all efficiency values into a single list. 

The function takes three parameters: 
- `n`: a list of integers representing input sizes for the algorithms
- `sheffc`: a list of floats representing efficiency values for the "she" algorithm
- `bfeffc`: a list of floats representing efficiency values for the "bfe" algorithm

The function should calculate the efficiency for the "bo" algorithm using the formula: 
\[ \text{boefficiency} = \left( i + \frac{{i^2 - i}}{2} \right) \times \log_{10}(i) \]
where \( i \) is the input size.

The function should then return a list `topalg` by concatenating `sheffc`, `bfeffc`, and the calculated `boeffc`.
"""

import math

def calculate_efficiency(n, sheffc, bfeffc):
    boeffc = [((i + ((i**2 - i) / 2)) * math.log10(i)) for i in n]
    return sheffc + bfeffc + boeffc