"""
QUESTION:
Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values (oldest age first) if those exist or `null/None` if:

* `sum < 0`
* `difference < 0`
* Either of the calculated ages come out to be negative
"""

def calculate_ages(sum_of_ages, age_difference):
    # Check for invalid input conditions
    if sum_of_ages < 0 or age_difference < 0:
        return None
    
    # Calculate the individual ages
    age1 = (sum_of_ages + age_difference) / 2
    age2 = (sum_of_ages - age_difference) / 2
    
    # Check if either of the calculated ages is negative
    if age1 < 0 or age2 < 0:
        return None
    
    # Return the ages with the oldest age first
    return (max(age1, age2), min(age1, age2))