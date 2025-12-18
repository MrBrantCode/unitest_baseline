"""
QUESTION:
Implement a function `collaborative_filtering(data)` that takes a dictionary `data` where keys are product IDs and values are lists of reviews (or numerical user behavior) and returns a dictionary where keys are product IDs and values are lists of tuples. Each tuple contains a similar product ID and a score representing their similarity using cosine similarity. The function should handle potential issues such as division by zero and assume that the input `data` is well-structured. The function should also include necessary import statements and handle potential exceptions.
"""

import math

def collaborative_filtering(data):
    """
    This function calculates cosine similarity between products based on user reviews.

    Args:
        data (dict): A dictionary where keys are product IDs and values are lists of reviews.

    Returns:
        dict: A dictionary where keys are product IDs and values are lists of tuples.
              Each tuple contains a similar product ID and a score representing their similarity.
    """

    def cos_similarity(v1, v2):
        """
        This function calculates cosine similarity between two vectors.

        Args:
            v1 (list): The first vector.
            v2 (list): The second vector.

        Returns:
            float: The cosine similarity between the two vectors.
        """
        dot_product = sum(a * b for a, b in zip(v1, v2))
        magnitude_v1 = math.sqrt(sum(a ** 2 for a in v1))
        magnitude_v2 = math.sqrt(sum(b ** 2 for b in v2))
        if magnitude_v1 == 0 or magnitude_v2 == 0:
            return 0
        return dot_product / (magnitude_v1 * magnitude_v2)

    result = {}
    for prd, rev in data.items():
        similar_products = []
        for s_prd, s_rev in data.items():
            if prd != s_prd:
                similarity = cos_similarity(rev, s_rev)
                similar_products.append((s_prd, similarity))
        similar_products.sort(key=lambda x: x[1], reverse=True)
        result[prd] = similar_products
    return result