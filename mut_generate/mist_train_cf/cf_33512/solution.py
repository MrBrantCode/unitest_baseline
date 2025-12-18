"""
QUESTION:
Implement a Python program with two classes: `Product` and `ShoppingCart`. 

The `Product` class should have two attributes: `name` and `price`, which represent the name of the product and its price respectively.

The `ShoppingCart` class should have three methods: `add_to_cart(product)`, `remove_from_cart(product)`, and `calculate_total()`. The `add_to_cart(product)` method adds a product to the shopping cart, `remove_from_cart(product)` removes a product from the shopping cart, and `calculate_total()` calculates the total price of all products in the shopping cart. 

Do not use any external libraries or files. Write the program in a single Python file.
"""

def calculate_cart_total(products):
    total_price = sum(product.price for product in products)
    return total_price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def remove_from_cart(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return calculate_cart_total(self.products)