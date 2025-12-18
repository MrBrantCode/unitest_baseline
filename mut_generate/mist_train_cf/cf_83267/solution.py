"""
QUESTION:
Implement a `Transaction` class that can lazily load a `Customer` object given the `customer_id` using dependency injection for the `ICustomerDao` interface, without requiring the `Transaction` object to be aware of the Inversion of Control Container. The `Transaction` class should not directly reference the Inversion of Control Container. Assume the `ICustomerDao` interface has a `GetById` method that retrieves a `Customer` by its ID.
"""

def transaction(customer_id, customer_dao):
  """Lazily loads a Customer object given the customer_id using dependency injection for the ICustomerDao interface."""
  
  _customer = None

  def get_customer():
    nonlocal _customer
    if _customer is None:
      _customer = customer_dao.get_by_id(customer_id)
    return _customer

  return get_customer