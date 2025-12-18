"""
QUESTION:
Write a function named `second_oldest_age` that takes a list of dictionaries as input, where each dictionary represents a person with an "age" key. The function should return the age of the second oldest person in the list. The age must be a positive integer between 18 and 100 (inclusive). If there is a tie for second oldest, return the age of the oldest person among those tied. If the input list is empty or does not contain any dictionaries, or if there is less than two people with valid ages, return None.
"""

def second_oldest_age(lst):
    if len(lst) == 0 or not all(isinstance(d, dict) for d in lst):
        return None
    
    ages = [d["age"] for d in lst if isinstance(d["age"], int) and 18 <= d["age"] <= 100]
    
    if len(ages) < 2:
        return None
    
    sorted_ages = sorted(ages)
    second_oldest = sorted_ages[-2]
    
    return second_oldest