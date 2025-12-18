"""
QUESTION:
Create a function `serialize_data_contract` that handles optional elements in XML Schema when sending data back to a WCF service from a client. The function should take into account that WCF represents optional properties as a pair of properties: a Boolean property named `XXXSpecified` and another property with the actual type named `XXX`. Ensure that the function sets `XXXSpecified` to `true` for mandatory fields when `minOccurs="0"` in the schema, or provide an alternative solution if the schema can be modified.
"""

def serialize_data_contract(data_contract):
    """
    This function handles optional elements in XML Schema when sending data back to a WCF service from a client.
    
    It sets 'XXXSpecified' to 'true' for mandatory fields when 'minOccurs="0"' in the schema.
    
    Args:
        data_contract (dict): A dictionary representing the data contract.
        
    Returns:
        dict: The modified data contract with 'XXXSpecified' set to 'true' for mandatory fields.
    """
    
    # Iterate over each key-value pair in the data contract
    for key, value in data_contract.items():
        
        # Check if the key is a mandatory field
        if key.endswith('Specified'):
            # Set 'XXXSpecified' to 'true'
            data_contract[key] = True
            
    return data_contract