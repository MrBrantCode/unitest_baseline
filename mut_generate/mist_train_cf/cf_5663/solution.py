"""
QUESTION:
Create a function `check_eligibility` that takes in the following parameters: `age`, `gender`, `country`, `criminal_record`, `education_level`, `military_service`, `previous_political_experience`, `financial_qualifications`, and `professional_qualifications`. The function should return a boolean value indicating whether a person is eligible to vote in their country of residence, considering the country's specific requirements. Additionally, the function should return a boolean value indicating whether the person is eligible to run for political office in their country, based on factors such as previous political experience and financial or professional qualifications required by the country. The function should support at least two countries: the United States and Canada.
"""

def check_eligibility(age, gender, country, criminal_record, education_level, military_service, previous_political_experience, financial_qualifications, professional_qualifications):
    """
    This function checks whether a person is eligible to vote in their country of residence
    and whether they are eligible to run for political office in their country.

    Args:
        age (int): The age of the person.
        gender (str): The gender of the person.
        country (str): The country of residence of the person.
        criminal_record (bool): Whether the person has a criminal record.
        education_level (int): The education level of the person.
        military_service (bool): Whether the person has fulfilled mandatory military service.
        previous_political_experience (int): The number of years of previous political experience.
        financial_qualifications (bool): Whether the person has the required financial qualifications.
        professional_qualifications (bool): Whether the person has the required professional qualifications.

    Returns:
        tuple: A tuple containing two boolean values. The first value indicates whether the person is eligible to vote,
               and the second value indicates whether the person is eligible to run for political office.
    """

    # Check voting eligibility
    if country == "United States":
        eligible_to_vote = age >= 18 and not criminal_record
    elif country == "Canada":
        eligible_to_vote = age >= 18 and not criminal_record and education_level >= 12
    else:
        eligible_to_vote = False  # Add more countries with their respective eligibility criteria

    # Check eligibility to run for political office
    if country == "United States":
        eligible_to_run = age >= 25 and previous_political_experience >= 2 and not criminal_record
    elif country == "Canada":
        eligible_to_run = age >= 18 and not criminal_record and education_level >= 12 and financial_qualifications and professional_qualifications
    else:
        eligible_to_run = False  # Add more countries with their respective eligibility criteria

    return eligible_to_vote, eligible_to_run