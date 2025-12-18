"""
QUESTION:
Write a function `insertDash(num)`/`InsertDash(int num)` that will insert dashes ('-') between each two odd numbers in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

Note that the number will always be non-negative (>= 0).
"""

import re

def insert_dash(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Use regular expression to insert dashes between each two odd digits
    result = re.sub('([13579])(?=[13579])', '\\1-', num_str)
    
    return result