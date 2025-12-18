"""
QUESTION:
Create a Python function called `sort_dict_list` that takes a list of dictionaries as input. The function should filter the list to only include dictionaries with a key "status" and value "active", then sort the filtered list in ascending order based on the "count" key. In cases where "count" values are equal, sort by the length of the "name" key in descending order. The sorting should be stable, preserving the relative order of dictionaries with equal "count" and "name" length.
"""

def sort_dict_list(lst):
    active_dicts = [d for d in lst if d.get("status") == "active"]
    sorted_dicts = sorted(active_dicts, key=lambda x: (x["count"], -len(x["name"])), reverse=False)
    return sorted_dicts