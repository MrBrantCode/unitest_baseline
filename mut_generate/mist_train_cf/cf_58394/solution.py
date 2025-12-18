"""
QUESTION:
Create a function `map_dynamic_claim` that handles dynamic Azure AD B2C client IDs in Graph API responses. The function should map claims with dynamic client IDs to a standard claim name, as the client ID is passed as a parameter and can change dynamically. The input will be a dictionary with dynamic client ID keys (e.g., `extension_0000-00000-0000-000_name`) and the output should be a dictionary with a standard claim name.
"""

def map_dynamic_claim(input_dict, client_id, standard_claim_name):
    """
    Maps claims with dynamic client IDs to a standard claim name.

    Args:
    input_dict (dict): A dictionary with dynamic client ID keys.
    client_id (str): The dynamic client ID.
    standard_claim_name (str): The standard claim name to map to.

    Returns:
    dict: A dictionary with a standard claim name.
    """
    output_dict = {}
    for key, value in input_dict.items():
        if key.startswith(f"extension_{client_id}_"):
            output_dict[standard_claim_name] = value
        else:
            output_dict[key] = value
    return output_dict