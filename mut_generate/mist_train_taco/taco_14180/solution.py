"""
QUESTION:
# Task

Given the birthdates of two people, find the date when the younger one is exactly half the age of the other.

# Notes

* The dates are given in the format YYYY-MM-DD and are not sorted in any particular order
* Round **down** to the nearest day
* Return the result as a string, like the input dates
"""

from dateutil.parser import parse

def find_half_age_date(birthdate1: str, birthdate2: str) -> str:
    # Parse the input birthdates
    p1 = parse(birthdate1)
    p2 = parse(birthdate2)
    
    # Ensure p1 is the older person and p2 is the younger person
    if p1 > p2:
        p1, p2 = p2, p1
    
    # Calculate the date when the younger person is exactly half the age of the older person
    half_age_date = p2 + (p2 - p1)
    
    # Return the result as a string in the format YYYY-MM-DD
    return str(half_age_date)[:10]