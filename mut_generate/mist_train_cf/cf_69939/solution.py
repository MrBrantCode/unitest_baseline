"""
QUESTION:
Create a function named `calculate_minimal_cost` that takes in two parameters: a list of product prices (`product_prices`) and a list of discounts (`discounts`). The function should calculate and return the lowest possible total cost after applying the discounts in a sequence, where each discount is applied to the corresponding product in a way that maximizes the overall discount.

The list `product_prices` contains the original prices of products, and the list `discounts` contains discount percentages. The discounts are applied in a sequence, where the first discount is applied to the product with the highest price, the second discount to the product with the next highest price, and so on. If there are more products than discounts, the remaining products are added to the total cost without any discount.

The function should return the minimum total cost of all products after applying the discounts. The discounts range from 1 to 100, and there can be up to 1000 discounts. The product prices range from 0 to 10^9.
"""

def calculate_minimal_cost(product_prices, discounts):
    product_prices.sort(reverse=True)  # Sort in descending order.
    discounts.sort(reverse=True)  # Sort in descending order.
  
    i, j = 0, 0
    minimal_cost = 0
    while i < len(product_prices) and j < len(discounts):
        # Apply the discount on the product.
        minimal_cost += product_prices[i] * (1 - (discounts[j] / 100))
        i += 1
        j += 1

    # If there are more products than discounts.
    while i < len(product_prices):
        minimal_cost += product_prices[i]
        i += 1

    return minimal_cost