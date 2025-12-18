"""
QUESTION:
Write a function `extract_dollar_rows` that takes a 2D numpy array `matrix` as input, where each row contains an item ID and a price. The function should return a new 2D numpy array containing only the rows where the price is denoted by a dollar sign.
"""

import numpy as np
import re

def extract_dollar_rows(matrix):
    pattern = re.compile(r'\$\d+')
    return np.array([row for row in matrix if pattern.search(row[1])])