"""
QUESTION:
Create a function named `enrich_dict` that takes a dictionary as input and returns the dictionary with three additional key-value pairs. The first key should be "integers" and its value should be a list of integers. The second key should be "nested_dict" and its value should be a dictionary with at least two key-value pairs. The third key should be "concat_function" and its value should be a function that takes two string arguments and returns their concatenation. The input dictionary should not be modified in place.
"""

def enrich_dict(input_dict):
    """
    This function takes a dictionary as input and returns the dictionary 
    with three additional key-value pairs.
    
    Args:
    input_dict (dict): The input dictionary.
    
    Returns:
    dict: The enriched dictionary with three additional key-value pairs.
    """
    
    # Create a copy of the input dictionary to avoid modifying it in place
    enriched_dict = input_dict.copy()
    
    # add a key-value relationship where the key is "integers" and the value is a list of integers
    enriched_dict["integers"] = [1, 2, 3, 4, 5]
    
    # add a key-value relationship where the key is "nested_dict" and the value is a nested dictionary
    enriched_dict["nested_dict"] = {"key1": "value1", "key2": "value2"}
    
    # Define a function that takes two string arguments and returns their concatenation
    def concat_str(str1, str2):
        return str1 + str2
    
    # add a key-value relationship where the key is "concat_function" and the value is a function
    enriched_dict["concat_function"] = concat_str
    
    return enriched_dict