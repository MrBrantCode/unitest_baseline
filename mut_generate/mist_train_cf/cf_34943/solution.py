"""
QUESTION:
Write a function `calculateDiscountedPrice` that calculates the final discounted price of a product based on its original price and the discount percentage. The function should take two parameters: `originalPrice`, a positive floating-point number, and `discountPercentage`, a positive integer. The function should return a string representing the final discounted price formatted as a currency with the dollar sign, comma-separated thousands, and two decimal places.
"""

def calculateDiscountedPrice(originalPrice, discountPercentage):
    discountedPrice = originalPrice - (originalPrice * discountPercentage / 100)
    formattedPrice = "${:,.2f}".format(discountedPrice)
    return formattedPrice