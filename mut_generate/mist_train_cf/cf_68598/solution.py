"""
QUESTION:
Write a function `is_eligible` that takes an integer `age` as input and returns `True` if the age is greater than or equal to 18, indicating the person is eligible for voting, and `False` otherwise. The function should use a Boolean flag variable to manage the eligibility condition.
"""

def is_eligible(age):
    eligible = False
    if age >= 18:
        eligible = True
    return eligible