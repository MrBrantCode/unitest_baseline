"""
QUESTION:
Implement a function `compare_results(experimental, expected, tolerance)` that compares each experimental result with the corresponding expected value and determines if they are within the specified tolerance. 

- Parameters: 
  - `experimental`: a list of experimental results (float values)
  - `expected`: a list of expected values (float values)
  - `tolerance`: a float representing the maximum allowable difference between experimental and expected values
- Return value: a list of boolean values, where each value indicates whether the corresponding experimental result is within the specified tolerance of the expected value.
"""

def compare_results(experimental, expected, tolerance):
    return [abs(exp - exp_val) <= tolerance for exp, exp_val in zip(experimental, expected)]