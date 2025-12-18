"""
QUESTION:
Add a list to a specific key in a nested JSON document at a depth of at least 4 levels from the root using a recursive function. The function should take the JSON document, the target key, and the list to be added as input, and return the updated JSON document. The time complexity of the solution should be O(1), and it should handle nested JSON documents containing both dictionaries and lists.
"""

def entance(json_doc, target_key, my_list):
    if isinstance(json_doc, dict):
        for key, value in json_doc.items():
            if key == target_key:
                json_doc[key] = my_list
                return
            entance(value, target_key, my_list)
    elif isinstance(json_doc, list):
        for item in json_doc:
            entance(item, target_key, my_list)