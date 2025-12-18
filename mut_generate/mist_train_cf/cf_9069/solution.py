"""
QUESTION:
Implement a function named `calculate_total_price` that takes a list of dictionaries as input. Each dictionary contains a "price" key with a positive integer value. The function should calculate the sum of all the prices in the list and return the result as an integer. The function should have a time complexity of O(n), where n is the total number of elements in all dictionaries combined, and a space complexity of O(1).
"""

def calculate_total_price(data):
    total_price = 0
    for item in data:
        total_price += item["price"]
    return total_price