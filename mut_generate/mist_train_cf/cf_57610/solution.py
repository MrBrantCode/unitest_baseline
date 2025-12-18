"""
QUESTION:
Design a JSON-LD prototype for representing an individual's biographical details, including name, age, and gender, as well as education, employment history, relationships, and schema.org-compliant person-associated fields. The prototype must adhere to JSON-LD syntax guidelines and utilize schema.org vocabulary. The function should be able to accommodate the following data: 

Designation: John Doe
Chronological Age: 33
Gender Identification: Male
Academic History: BSc Computer Science - Stanford University, MBA - Harvard Business School
Employment History: Google's Software Engineer (2005-2010), Facebook's Senior Software Engineer (2010-2015), Start-up XYZ's CTO (2016-Present)
Relational Status: Single with two siblings
Person-associated Variables in accordance with schema.org: U.S. citizenship, Proficient in English and Spanish, Possesses a pet dog called Max.
"""

def person_biography(
    name, 
    age, 
    gender, 
    nationality, 
    knows_language, 
    has_pet, 
    family_status, 
    alumni_of, 
    has_occupation
):
    """
    A function to create a JSON-LD prototype for representing an individual's 
    biographical details.

    Args:
    - name (str): The individual's name.
    - age (int): The individual's age.
    - gender (str): The individual's gender.
    - nationality (str): The individual's nationality.
    - knows_language (list): A list of languages the individual knows.
    - has_pet (dict): A dictionary containing details about the individual's pet.
    - family_status (str): The individual's family status.
    - alumni_of (list): A list of dictionaries containing details about the individual's education.
    - has_occupation (list): A list of dictionaries containing details about the individual's occupation.

    Returns:
    - dict: A JSON-LD prototype representing the individual's biographical details.
    """

    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": name,
        "gender": gender,
        "age": age,
        "nationality": nationality,
        "knowsLanguage": knows_language,
        "hasPet": has_pet,
        "familyStatus": family_status,
        "alumniOf": alumni_of,
        "hasOccupation": has_occupation
    }