"""
QUESTION:
Implement a function `sort_vulnerabilities(vulnerabilities, sort_field, sort_order)` that takes in a list of dictionaries, `sort_field` (the key based on which the sorting should be performed), and `sort_order` (either "ASC" for ascending or "DESC" for descending). The function should return the sorted list of dictionaries based on the specified key and sort order. Each dictionary in the list is expected to contain the `sort_field` key.
"""

def sort_vulnerabilities(vulnerabilities, sort_field, sort_order):
    return sorted(vulnerabilities, key=lambda x: x[sort_field], reverse=(sort_order == "DESC"))