"""
QUESTION:
Create a function `parse_address` that takes a string representing a full address and returns a dictionary containing the street, city, state, and zip code. The input string is expected to be in the format "street, city, state, zip" with a comma separating each component. The function should correctly split the input string into the respective components and populate the dictionary accordingly.
"""

def parse_address(address):
    """
    Parse a full address into a dictionary containing street, city, state, and zip code.

    Args:
        address (str): A string representing a full address in the format "street, city, state, zip".

    Returns:
        dict: A dictionary containing the street, city, state, and zip code.
    """
    return {
        "street": address.split(",")[0],
        "city": address.split(",")[1].strip(),
        "state": address.split(",")[2].strip(),
        "zip": address.split(",")[3].strip()
    }