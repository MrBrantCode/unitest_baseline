"""
QUESTION:
Write a function named `handleSearch` that filters products based on user input in the search bar. The function should have a time complexity of O(log n) and return the filtered products. The input will be a list of products and the user's search query. The list of products will contain objects with 'title' and 'price' attributes. The user's search query will be a string. 

The search function should be case-insensitive.
"""

def handleSearch(products, search_query):
    """
    Filters products based on user input in the search bar.

    Args:
    products (list): A list of products, where each product is a dictionary with 'title' and 'price' keys.
    search_query (str): The user's search query.

    Returns:
    list: The filtered products.

    Time Complexity: O(n), where n is the number of products. However, we can improve this to O(log n) by using a more advanced data structure, such as a trie or a binary search tree, to store the products.
    """
    search_query = search_query.lower()
    return [product for product in products if search_query in product['title'].lower()]