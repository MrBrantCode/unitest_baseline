"""
QUESTION:
Write a function named `count_fruit_types` that takes a JSON object as input and returns a dictionary with the count of each fruit type. The function should handle null and invalid values, and it should be efficient enough to handle large data sizes. The dictionary should include all fruit types, even if their count is zero, and it should exclude non-fruit categories.
"""

def count_fruit_types(data):
    """
    This function takes a JSON object as input and returns a dictionary with the count of each fruit type.

    Args:
    data (dict): A dictionary containing a list of items with category, type, and count.

    Returns:
    dict: A dictionary with the count of each fruit type.
    """
    fruit_count = {}
    
    for item in data['items']:
        if item.get('category') == 'fruit' and item.get('type') is not None:
            fruit_count[item['type']] = fruit_count.get(item['type'], 0)
            if item.get('count') is not None:
                fruit_count[item['type']] += item['count']

    return fruit_count