"""
QUESTION:
Create a function named `select_customers` that takes a 2D list `customer_table` and a tuple `zipcode_range` as inputs. The function should return a list of customers where the age is greater than 30, the zip code falls within the given range, and the name does not start with the letter 'A'. The `customer_table` is a list of lists where each sublist contains a customer's name, age, and zip code, and the `zipcode_range` is a tuple containing the lower and upper bounds of the zip code range.
"""

def select_customers(customer_table, zipcode_range):
    """
    Selects customers from the given table where the age is greater than 30, 
    the zip code falls within the given range, and the name does not start with 'A'.

    Args:
        customer_table (list): A list of lists where each sublist contains a customer's name, age, and zip code.
        zipcode_range (tuple): A tuple containing the lower and upper bounds of the zip code range.

    Returns:
        list: A list of customers that meet the specified criteria.
    """
    return [customer for customer in customer_table 
            if customer[1] > 30 and zipcode_range[0] <= customer[2] <= zipcode_range[1] and not customer[0].startswith('A')]