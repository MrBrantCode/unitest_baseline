"""
QUESTION:
Create a function `create_person` that takes in the following parameters: `occupation`, `experience`, `location`, `specialization` (optional), and `certification` (optional), and returns a dictionary containing these parameters as key-value pairs, where `occupation`, `experience`, and `location` are mandatory and `specialization` and `certification` are optional.
"""

def create_person(occupation, experience, location, specialization=None, certification=None):
    person = {
        "Occupation": occupation,
        "Experience(Years)": experience,
        "Location": location,
        "Specialization": specialization,
        "Certification": certification
    }
    return person