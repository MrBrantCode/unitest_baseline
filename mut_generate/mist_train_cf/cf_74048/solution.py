"""
QUESTION:
Create a Python function named `create_person_schema` that generates a JSON-LD schema aligned with the Person class of the Schema.org ontology. The function should take in an individual's information (name, age, and gender) and occupation-specific information (job title, years of experience, and skills acquired). The output JSON-LD schema should be well-mapped and compliant with standard norms. Ensure the schema passes Google's Structured Data Testing Tool without any errors or recommendations.
"""

import json

def create_person_schema(name, age, gender, job_title, years_of_experience, skills):
    """
    Creates a JSON-LD schema aligned with the Person class of the Schema.org ontology.

    Args:
        name (str): The person's name.
        age (int): The person's age.
        gender (str): The person's gender.
        job_title (str): The person's job title.
        years_of_experience (int): The person's years of experience.
        skills (list): The person's skills.

    Returns:
        dict: The JSON-LD schema.
    """

    data = {
        "@context": "https://schema.org/",
        "@type": "Person",
        "name": name,
        "gender": gender,
        "age": age,
        "jobTitle": job_title,
        "workExperience": {
            "@type": "QuantitativeValue",
            "value": years_of_experience,
            "unitText": "years"
        },
        "knowsAbout": skills
    }

    return json.dumps(data, indent=4)