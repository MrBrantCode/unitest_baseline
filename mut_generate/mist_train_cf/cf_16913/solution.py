"""
QUESTION:
Create a function named `generate_user_json` that takes in a dictionary containing a user's information, including name, age, location, job title, company, salary, skills, education, and additional details such as previous job title, company, duration, salary, certifications, and projects. The function should return a JSON object that describes the user's information. The JSON object should have the following structure: 
- name (string)
- age (integer)
- location (string)
- jobTitle (string)
- company (string)
- salary (string)
- skills (list of strings)
- education (object with degree, university, and graduationYear)
- additionalDetails (object with previousJobTitle, previousCompany, previousJobDuration, previousSalary, certifications, and projects)
- certifications (list of strings)
- projects (list of objects with name, description, and duration)
"""

import json

def generate_user_json(user_info):
    """
    Generate a JSON object that describes a user's information.

    Args:
        user_info (dict): A dictionary containing a user's information.

    Returns:
        str: A JSON object that describes the user's information.
    """

    # Ensure 'additionalDetails' and 'education' are present in the user_info dictionary
    user_info.setdefault('additionalDetails', {})
    user_info.setdefault('education', {})

    # Ensure 'certifications' and 'projects' are present in 'additionalDetails'
    user_info['additionalDetails'].setdefault('certifications', [])
    user_info['additionalDetails'].setdefault('projects', [])

    # Create the JSON object
    user_json = {
        "name": user_info['name'],
        "age": user_info['age'],
        "location": user_info['location'],
        "jobTitle": user_info['jobTitle'],
        "company": user_info['company'],
        "salary": user_info['salary'],
        "skills": user_info['skills'],
        "education": {
            "degree": user_info['education'].get('degree', ''),
            "university": user_info['education'].get('university', ''),
            "graduationYear": user_info['education'].get('graduationYear', '')
        },
        "additionalDetails": {
            "previousJobTitle": user_info['additionalDetails'].get('previousJobTitle', ''),
            "previousCompany": user_info['additionalDetails'].get('previousCompany', ''),
            "previousJobDuration": user_info['additionalDetails'].get('previousJobDuration', ''),
            "previousSalary": user_info['additionalDetails'].get('previousSalary', ''),
            "certifications": user_info['additionalDetails']['certifications'],
            "projects": user_info['additionalDetails']['projects']
        }
    }

    # Convert the JSON object to a string and return it
    return json.dumps(user_json, indent=4)