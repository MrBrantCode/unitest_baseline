"""
QUESTION:
Design a data structure to store a person's information, which includes a string for name, an integer for age, a list for pets, and nested data structures for medical history and job history. The data structure should efficiently store and access the information, considering time and space complexity. It should also be able to accommodate different data formats and nested levels.
"""

def person_info(name, age, pets, medical_history, job_history):
    """
    A function to create a person's information data structure.

    Args:
    name (str): The person's name.
    age (int): The person's age.
    pets (list): A list of the person's pets.
    medical_history (object): A linked list object representing the person's medical history.
    job_history (object): A queue object representing the person's job history.

    Returns:
    dict: A dictionary containing the person's information.
    """

    # Create a dictionary to store the person's information
    person = {
        'name': name,  
        'age': age,  
        'pets': pets,  
        'medical_history': medical_history,  
        'job_history': job_history  
    }

    # Return the person's information
    return person