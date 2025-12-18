"""
QUESTION:
Implement a function `clean_type_name` that takes a type name as a string input and returns the cleaned type name. The cleaning rules are as follows: 
- Truncate the type name to `synopsis_maxlen_function` characters if its length exceeds `synopsis_maxlen_function`.
- Append "_cleaned" to the type name if it is found in `synopsis_class_list`.
- Replace all occurrences of "ns" with an empty string in the type name if it matches `process_type_name_ns_to_clean`.

Function Signature: `def clean_type_name(type_name: str) -> str`
"""

def clean_type_name(type_name: str, synopsis_maxlen_function: int, synopsis_class_list: list, process_type_name_ns_to_clean: str) -> str:
    """
    Cleans a type name based on the given rules.

    Args:
    - type_name (str): The type name to be cleaned.
    - synopsis_maxlen_function (int): The maximum length for the type name.
    - synopsis_class_list (list): The list of type names to be appended with "_cleaned".
    - process_type_name_ns_to_clean (str): The type name that should replace "ns" with an empty string.

    Returns:
    - str: The cleaned type name.
    """
    # Rule 1: Truncate if length exceeds synopsis_maxlen_function
    if len(type_name) > synopsis_maxlen_function:
        type_name = type_name[:synopsis_maxlen_function]
    
    # Rule 2: Append "_cleaned" if type_name is in synopsis_class_list
    if type_name in synopsis_class_list:
        type_name += "_cleaned"
    
    # Rule 3: Replace "ns" with an empty string if type_name matches process_type_name_ns_to_clean
    if type_name == process_type_name_ns_to_clean:
        type_name = type_name.replace("ns", "")
    
    return type_name