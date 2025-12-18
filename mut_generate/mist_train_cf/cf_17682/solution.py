"""
QUESTION:
Implement a function `find_name_by_id(json_object, target_id)` that takes a JSON object as a string and an id as an integer, and returns the "name" corresponding to the given id. The function should parse the JSON object from scratch without using any loops or recursion, and without relying on any external libraries.
"""

def find_name_by_id(json_object, target_id):
    # Find the index of "id" key
    id_index = json_object.index('"id":')

    # Find the index of value of "id" key
    id_value_index = json_object.index(':', id_index) + 1
    id_value = ''
    for char in json_object[id_value_index:]:
        if char.isdigit():
            id_value += char
        else:
            break

    # Check if the current "id" is the target "id"
    if int(id_value) == target_id:
        # Find the index of "name" key
        name_index = json_object.index('"name"')
        
        # Find the index of closing quote '"' after "name" key
        closing_quote_index1 = json_object.index('"', name_index+len('"name"')+1)

        # Find the index of closing quote '"' after the value of "name" key
        closing_quote_index2 = json_object.index('"', closing_quote_index1+1)

        # Extract substring between the two closing quotes
        name_value = json_object[closing_quote_index1+1:closing_quote_index2]

        return name_value
    else:
        # If the current "id" is not the target "id", find the index of closing bracket '}' after the "id" key
        closing_bracket_index = json_object.index('}', id_index)
        
        # Extract substring after the closing bracket '}' for next iteration
        remaining_json = json_object[closing_bracket_index+1:]
        
        # Recursively call the function with the remaining JSON object
        return find_name_by_id(remaining_json, target_id)