"""
QUESTION:
Write a function `calculate_total_price` that calculates the total price of a purchase using the given JSON data for fruits and their prices. The JSON data contains a list of fruits with their names, prices, and quantities. The function should return the total price of the purchase.

The input JSON data will be a string in the format:
```
{
  "fruits": [
    {
      "name": string,
      "price": float,
      "quantity": int
    },
    ...
  ]
}
```
Restrictions:
- Use Python as the programming language.
- Optimize the code for efficiency.
"""

import json

def calculate_total_price(json_data):
    """
    Calculate the total price of a purchase using the given JSON data for fruits and their prices.

    Args:
        json_data (str): A JSON string containing a list of fruits with their names, prices, and quantities.

    Returns:
        float: The total price of the purchase.
    """
    fruits = json.loads(json_data)["fruits"]
    return sum(fruit["price"] * fruit["quantity"] for fruit in fruits)