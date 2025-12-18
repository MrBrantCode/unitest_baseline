"""
QUESTION:
Implement a function named `calculate_discounted_price` that takes a list of dictionaries as input, where each dictionary contains the keys "price" and "discount" with positive integer values, and the discount value is less than or equal to the price. The function should calculate the sum of all the discounted prices, where the discounted price is the price minus the discount, and return the result as an integer. The function should have a time complexity of O(n), where n is the total number of elements in all dictionaries combined, and a space complexity of O(1).
"""

def calculate_discounted_price(dictionaries):
    total_discounted_price = 0
    for dictionary in dictionaries:
        price = dictionary["price"]
        discount = dictionary["discount"]
        discounted_price = price - discount
        total_discounted_price += discounted_price
    return total_discounted_price