"""
QUESTION:
Create a function `check_voting_eligibility` that takes in three parameters: `age`, `gender`, and `country`, and returns a boolean indicating whether a person is eligible to vote in their country of residence. Assume voting eligibility is 18 years or older, and the countries of interest are the United States, the United Kingdom, and Canada, with the United States not having any gender restrictions.
"""

def check_voting_eligibility(age, gender, country):
    if country.lower() in ['united states', 'united kingdom', 'canada']:
        return age >= 18
    else:
        return False