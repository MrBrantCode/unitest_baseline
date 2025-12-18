"""
QUESTION:
Write a function `filter_customers` that takes a list of customer records and a tuple representing a zip code range as input. Each customer record is a list containing the customer's name, age, and zip code. The function should return a list of customer records where the customer's age is greater than 30, their zip code is within the given range, and their last name contains the letter 'e'. Additionally, the function should exclude customers whose names start with the letter 'A'.
"""

def filter_customers(customers, zip_code_range):
    """
    Filters customer records based on age, zip code range, and last name.

    Args:
    - customers (list): A list of customer records.
    - zip_code_range (tuple): A tuple representing the zip code range.

    Returns:
    - list: A list of filtered customer records.
    """
    return [
        customer for customer in customers
        if customer[1] > 30  # age > 30
        and zip_code_range[0] <= customer[2] <= zip_code_range[1]  # zip code within range
        and 'e' in customer[0].split()[-1]  # last name contains 'e'
        and not customer[0].split()[0].startswith('A')  # name doesn't start with 'A'
    ]