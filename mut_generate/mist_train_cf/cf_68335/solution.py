"""
QUESTION:
Write a function `update_third_item` that takes a JSON object as input and returns the updated JSON object. The JSON object contains a list of stores, each with a list of departments, and each department has a list of items. The function should find the third item in the "items" array of the "sales" department in store "B" and increase its value by 10. If the "items" array has less than three elements or if the store "B" or the "sales" department is not found, the function should return the original JSON object unchanged.
"""

def update_third_item(json_object):
    """
    Update the third item in the 'items' array of the 'sales' department in store 'B' by increasing its value by 10.

    Args:
        json_object (dict): The input JSON object.

    Returns:
        dict: The updated JSON object or the original JSON object if the conditions are not met.
    """
    for store in json_object.get('stores', []):
        if store.get('store') == 'B':
            for department in store.get('departments', []):
                if department.get('department') == 'sales':
                    items = department.get('items', [])
                    if len(items) >= 3:
                        department['items'][2] += 10
    return json_object