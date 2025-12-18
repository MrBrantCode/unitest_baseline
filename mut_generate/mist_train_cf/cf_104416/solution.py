"""
QUESTION:
Create a function `check_eligibility` that takes three parameters: `age`, `name`, and `years_of_experience`. This function should return `True` if the `age` is greater than or equal to 21, the `name` starts with a vowel (both lowercase and uppercase), and the `years_of_experience` is greater than or equal to 5. Otherwise, it should return `False`.
"""

def check_eligibility(age, name, years_of_experience):
    return (age >= 21) and (name[0].lower() in ['a', 'e', 'i', 'o', 'u']) and (years_of_experience >= 5)