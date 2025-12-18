"""
QUESTION:
Design a function `sort_json(json_list, attribute)` that sorts a list of JSON objects by the value of a specified attribute. The function should return the sorted list of JSON objects. The list of JSON objects and the attribute to sort by are passed as arguments to the function. If the attribute is not found in one or more objects, the function should return an error message.
"""

def sort_json(json_list, attribute):
    """Sort a list of JSON objects based on attribute value."""
    try:
        sorted_list = sorted(json_list, key=lambda x: x[attribute])
        return sorted_list
    except KeyError:
        return "Attribute not found in one or more of the objects."
    except Exception as e:
        return f"An error occurred: {e}"