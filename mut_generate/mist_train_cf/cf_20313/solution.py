"""
QUESTION:
Create a function `check_eligibility` that takes in three parameters: `age` (an integer), `gender` (a string), and `country` (a string). The function should return a boolean indicating whether the person is eligible to vote and run for political office in their country of residence, based on the country-specific requirements provided in a predefined dictionary. The dictionary contains the minimum age required for voting and running for office for each country.
"""

# Define a dictionary with country-specific voting and running for political office requirements
voting_requirements = {
    "United States": {
        "voting_age": 18,
        "running_for_office_age": 25
    },
    "Canada": {
        "voting_age": 18,
        "running_for_office_age": 18
    },
    "United Kingdom": {
        "voting_age": 18,
        "running_for_office_age": 18
    }
}

def check_eligibility(age, gender, country):
    if country in voting_requirements:
        voting_age = voting_requirements[country]["voting_age"]
        running_for_office_age = voting_requirements[country]["running_for_office_age"]
        return age >= voting_age and age >= running_for_office_age
    else:
        return False