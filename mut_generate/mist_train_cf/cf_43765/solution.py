"""
QUESTION:
Write a function `palin_subseq_search(x, y)` that checks if the second string `y`, or any of its reverse versions, are found as a continuous subset within the first string `x`. The function should ignore upper and lower cases, special characters, and include language-specific characters. The function should be efficient even with larger string sizes.
"""

import re

def palin_subseq_search(x, y):
    """Check if the second string, or any of its reverse versions, are found as a continuous subset within the first string."""
  
    x = re.sub(r'\W+', '', x).lower()
    y = re.sub(r'\W+', '', y).lower()
    
    return y in x or y[::-1] in x