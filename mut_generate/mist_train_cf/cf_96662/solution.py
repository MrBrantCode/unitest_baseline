"""
QUESTION:
Create a function called `add_suffix` that adds the string " (High)" to each element in a pandas DataFrame column if the element's value is greater than 5000. Use the pandas `apply` function to apply the `add_suffix` function to the specified column. The function should return the modified column. The input column will contain only integers.
"""

import pandas as pd

def add_suffix(salary):
    if salary > 5000:
        return str(salary) + ' (High)'
    else:
        return str(salary)