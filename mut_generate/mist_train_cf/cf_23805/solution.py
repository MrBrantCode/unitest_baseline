"""
QUESTION:
Create a function named `total_cost` that calculates the total cost of a shopping cart. The function should take a list of dictionaries as an argument, where each dictionary represents an item in the cart with keys 'price' and 'quantity'. The function should return the total cost of all items in the cart. The input list of dictionaries is guaranteed to be non-empty and will only contain items with 'price' and 'quantity' keys.
"""

def total_cost(cart):
  total = 0
  for item in cart:
    total += item['price'] * item['quantity']
  return total