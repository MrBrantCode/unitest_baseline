"""
QUESTION:
Implement a function `calculate_discounted_price` that takes a list of dictionaries as input, where each dictionary contains a "price" key with a positive integer value and a "discount" key with a positive integer value less than or equal to the price. The function should calculate the sum of all the discounted prices and return the result as an integer. The time complexity should be O(n), where n is the total number of elements in all dictionaries combined, and the space complexity should be O(1).
"""

def calculate_discounted_price(dictionaries):
    total_discounted_price = 0
    for dictionary in dictionaries:
        price = dictionary["price"]
        discount = dictionary["discount"]
        discounted_price = price - discount
        total_discounted_price += discounted_price
    return total_discounted_price