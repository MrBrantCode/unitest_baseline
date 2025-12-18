"""
QUESTION:
Create a function named `create_individual_json` that generates a JSON string representing an individual's personal and professional data. The JSON string should include the individual's 'Name', 'Age', 'Residing City', 'Profession', 'Skills', 'Previous Employers', and 'Education'. The 'Skills' should be a list of entities with 'Skill Name' and 'Proficiency' ('novice', 'intermediate', 'expert'). The 'Previous Employers' and 'Education' should be lists of entities with 'Company Name', 'Position', and 'Years of Experience', and 'Institution Name', 'Degree', and 'Year of Graduation', respectively. The function should take 'Name', 'Age', and 'Residing City' as input parameters.
"""

import json

def create_individual_json(name, age, residing_city, profession, skills, previous_employers, education):
    """
    This function generates a JSON string representing an individual's personal and professional data.

    Parameters:
    name (str): The individual's name.
    age (int): The individual's age.
    residing_city (str): The individual's residing city.
    profession (str): The individual's profession.
    skills (list): A list of dictionaries, each containing 'Skill Name' and 'Proficiency' for the individual's skills.
    previous_employers (list): A list of dictionaries, each containing 'Company Name', 'Position', and 'Years of Experience' for the individual's previous employers.
    education (list): A list of dictionaries, each containing 'Institution Name', 'Degree', and 'Year of Graduation' for the individual's education.

    Returns:
    str: A JSON string representing the individual's data.
    """
    individual = {
        "Name": name,
        "Age": age,
        "Residing City": residing_city,
        "Profession": profession,
        "Skills": skills,
        "Previous Employers": previous_employers,
        "Education": education
    }
    
    return json.dumps(individual, indent=4)