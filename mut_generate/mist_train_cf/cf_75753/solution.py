"""
QUESTION:
Design a function `GetCustomer` that implements lazy loading for retrieving a customer's data and related entities (e.g., orders) in a distributed system like a WCF service. The function should take in a customer ID and a boolean indicating whether to include related entities. Consider using Data Transfer Objects (DTOs) to control what data gets loaded and serialized. The function should also address the issue of eager loading caused by serialization.
"""

from dataclasses import dataclass

# Define a Customer DTO
@dataclass
class CustomerDTO:
    id: int
    name: str
    orders: list = None

def get_customer(customer_id: int, include_orders: bool) -> CustomerDTO:
    """
    Retrieves a customer's data and related entities (orders) using lazy loading.

    Args:
    customer_id (int): The ID of the customer to retrieve.
    include_orders (bool): A flag indicating whether to include related orders.

    Returns:
    CustomerDTO: A Data Transfer Object containing the customer's data and related entities.
    """

    # Simulate retrieving customer data from a database or another data source
    customer_data = {
        'id': customer_id,
        'name': 'John Doe'
    }

    # Create a Customer DTO with the retrieved data
    customer = CustomerDTO(**customer_data)

    # If include_orders is True, eagerly load the customer's orders
    if include_orders:
        # Simulate retrieving orders from a database or another data source
        orders = [{'id': 1, 'total': 100.0}, {'id': 2, 'total': 200.0}]
        customer.orders = orders

    return customer