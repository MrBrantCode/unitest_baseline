"""
QUESTION:
Implement a function `calculate_discounted_prices` that takes a list of dictionaries and a threshold value as input. Each dictionary in the list contains keys "price" and "discount" with positive integer values, where the discount is less than or equal to the price. The function should calculate the sum of all discounted prices and return it along with the number of discounted items with a price greater than the threshold value. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the total number of elements in all dictionaries combined.
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