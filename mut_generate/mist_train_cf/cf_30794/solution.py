"""
QUESTION:
Implement the `calculate_p_at_k(k)` and `calculate_ap()` methods for the `InformationRetrievalMetrics` class. The `calculate_p_at_k(k)` method should calculate the precision at k (p@k) for the retrieved items in the `item_list` attribute, given the relevant items in the `discovered_answer` attribute and return the precision value. The `calculate_ap()` method should calculate the average precision (AP) for the retrieved items and return the average precision value.
"""

def calculate_p_at_k(k, retrieved_items, relevant_items):
    """
    Calculate the precision at k (p@k) for the retrieved items.

    Args:
        k (int): The number of retrieved items to consider.
        retrieved_items (list): The list of retrieved items.
        relevant_items (list): The list of relevant items.

    Returns:
        float: The precision at k value.
    """
    relevant_items_retrieved = sum(1 for item in retrieved_items[:k] if item in relevant_items)
    return relevant_items_retrieved / k if k > 0 else 0

def calculate_ap(retrieved_items, relevant_items):
    """
    Calculate the average precision (AP) for the retrieved items.

    Args:
        retrieved_items (list): The list of retrieved items.
        relevant_items (list): The list of relevant items.

    Returns:
        float: The average precision value.
    """
    precision_values = []
    relevant_items_found = 0
    for i, item in enumerate(retrieved_items):
        if item in relevant_items:
            relevant_items_found += 1
            precision_at_i = relevant_items_found / (i + 1)
            precision_values.append(precision_at_i)
    return sum(precision_values) / len(precision_values) if precision_values else 0