"""
QUESTION:
Write a function named `check_eligibility` that takes in four parameters: `age`, `name`, `years_of_work_experience`, and `job_title`. The function should return `True` if the following conditions are met: the `age` is 21 or older, the `name` starts with a vowel (case-insensitive), the `years_of_work_experience` is 5 or more, and the `job_title` contains the word 'manager' (case-insensitive). Otherwise, the function should return `False`.
"""

def check_eligibility(age, name, years_of_work_experience, job_title):
    """
    Checks if a person is eligible based on age, name, work experience, and job title.

    Args:
        age (int): The age of the person.
        name (str): The name of the person.
        years_of_work_experience (int): The years of work experience.
        job_title (str): The job title of the person.

    Returns:
        bool: True if the person is eligible, False otherwise.
    """
    return (age >= 21 and 
            name[0].lower() in ['a', 'e', 'i', 'o', 'u'] and 
            years_of_work_experience >= 5 and 
            'manager' in job_title.lower())