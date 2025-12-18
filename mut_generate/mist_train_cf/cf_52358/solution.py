"""
QUESTION:
Write a function to sum the quantity of items sold per product using the MongoDB `db.collection.aggregate()` method. The function should take a collection of product documents with '_id', 'name', and 'quantity' fields. The function should return a list of documents with 'name' and 'total' fields, where 'total' is the sum of the 'quantity' fields for each product.
"""

def sum_quantity_per_product(products):
    """
    Sum the quantity of items sold per product.

    Args:
        products (list): A list of product documents with '_id', 'name', and 'quantity' fields.

    Returns:
        list: A list of documents with 'name' and 'total' fields, where 'total' is the sum of the 'quantity' fields for each product.
    """

    result = []
    product_dict = {}

    # Group the products by 'name'
    for product in products:
        if product['name'] in product_dict:
            product_dict[product['name']] += product['quantity']
        else:
            product_dict[product['name']] = product['quantity']

    # Create the output list
    for name, total in product_dict.items():
        result.append({'name': name, 'total': total})

    return result