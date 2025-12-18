"""
QUESTION:
Assume you are creating a webshop and you would like to help the user in the search. You have products with brands, prices and name. You have the history of opened products (the most recently opened being the first item).

Your task is to create a list of brands ordered by popularity, if two brands have the same popularity level then choose the one which was opened last from the two and second the other one.

Product popularity is calculated from the history. If a product is more times in the history than it is more popular.

Your function will have one parameter which will be always an array/list of object.

example product:
{
  name: "Phone",
  price: 25,
  brand: "Fake brand"
}
"""

from collections import Counter

def sort_brands_by_popularity(history):
    # Extract brands from the history
    brands = [product['brand'] for product in history]
    
    # Count the frequency of each brand
    counter = Counter(brands)
    
    # Sort brands by popularity (frequency) and by the most recent appearance
    sorted_brands = sorted(set(brands), key=lambda x: (-counter[x], brands.index(x)))
    
    return sorted_brands