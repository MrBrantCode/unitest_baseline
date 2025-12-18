"""
QUESTION:
Implement a function named `calculate_discounted_prices` that takes a list of dictionaries and a positive integer threshold as input, where each dictionary contains a key "price" with a positive integer value and a key "discount" with a positive integer value less than or equal to the price. The function should calculate the sum of all the discounted prices and return the result as an integer, along with the number of discounted items that have a price greater than the given threshold value. The function should have a time complexity of O(n), where n is the total number of elements in all dictionaries combined, and a space complexity of O(1).
"""

def calculate_discounted_prices(lst, threshold):
    total_discounted_price = 0
    num_discounted_items_above_threshold = 0

    for item in lst:
        price = item["price"]
        discount = item["discount"]

        discounted_price = price - discount
        total_discounted_price += discounted_price

        if discounted_price > threshold:
            num_discounted_items_above_threshold += 1

    return total_discounted_price, num_discounted_items_above_threshold