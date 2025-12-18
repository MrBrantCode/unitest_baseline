"""
QUESTION:
Write a function `min_tables_required` that calculates the minimum number of circular tables required to seat all attendees at a wedding. The function takes two parameters: `attendees`, the total number of attendees, and `seats_per_table`, the number of individuals each table can accommodate. The function must return the minimum number of tables required to seat all attendees, rounded up to the nearest whole number.
"""

import math

def min_tables_required(attendees, seats_per_table):
    return math.ceil(attendees / seats_per_table)