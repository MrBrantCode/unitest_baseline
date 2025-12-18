"""
QUESTION:
Write a function called `change_fixture` that changes the fixture "shape" between test methods in a test class. The function should either modify the existing fixture or generate a new one based on different parameters.
"""

def change_fixture(fixture, params):
    """
    Generates a new fixture based on different parameters.

    Args:
        fixture (object): The existing fixture.
        params (dict): Parameters describing the new fixture.

    Returns:
        object: A new fixture according to the specifications.
    """
    # Here you can implement your logic to generate a new fixture based on params
    # This is a basic example where fixture is a dictionary and params is also a dictionary
    new_fixture = fixture.copy()
    new_fixture.update(params)
    return new_fixture