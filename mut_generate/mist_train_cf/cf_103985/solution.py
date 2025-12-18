"""
QUESTION:
Create a function called `create_document` that returns a dictionary representing a MongoDB document for a person. The document should contain the following fields: First Name, Last Name, Age, Occupation, Email, Address, City, State, Country, Phone, Skills, and Projects. The Phone field should be a string, Skills should be a list of strings, and Projects should be a list of dictionaries with Project Name, Start Date, and End Date fields.
"""

def create_document(first_name, last_name, age, occupation, email, address, city, state, country, phone, skills, projects):
    """
    Returns a dictionary representing a MongoDB document for a person.

    Args:
        first_name (str): The person's first name.
        last_name (str): The person's last name.
        age (int): The person's age.
        occupation (str): The person's occupation.
        email (str): The person's email address.
        address (str): The person's street address.
        city (str): The person's city.
        state (str): The person's state.
        country (str): The person's country.
        phone (str): The person's phone number.
        skills (list[str]): A list of the person's skills.
        projects (list[dict]): A list of dictionaries containing project information.

    Returns:
        dict: A dictionary representing a MongoDB document for a person.
    """
    return {
        "First Name": first_name,
        "Last Name": last_name,
        "Age": age,
        "Occupation": occupation,
        "Email": email,
        "Address": address,
        "City": city,
        "State": state,
        "Country": country,
        "Phone": phone,
        "Skills": skills,
        "Projects": projects
    }