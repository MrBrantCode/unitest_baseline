"""
QUESTION:
Define a function named `create_person_info` that takes a person's name, age, and address as input and returns a tuple containing this information. The function should ensure that the returned tuple is immutable, and provide advantages and disadvantages of using tuples in this context.
"""

def create_person_info(name, age, address):
    """
    Creates a tuple containing a person's information.

    Args:
    name (str): The person's name.
    age (int): The person's age.
    address (str): The person's address.

    Returns:
    tuple: A tuple containing the person's name, age, and address.
    """
    return (name, age, address)