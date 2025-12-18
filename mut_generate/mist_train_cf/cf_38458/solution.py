"""
QUESTION:
Create a function `validate_mongodb_connection_string` that takes a MongoDB connection string as input and returns `True` if the string is valid, and `False` otherwise. The function must check that the string follows the format `mongodb://username:password@host:port/database?options` and contains the `username`, `password`, and `authSource` parameters.
"""

def validate_mongodb_connection_string(connection_string: str) -> bool:
    required_params = {'username', 'password', 'authSource'}
    
    # Split the connection string to extract parameters
    params = connection_string.split('//')[-1].split('@')[-1].split('/')[0].split('?')[0].split('&')
    
    # Create a set of parameters present in the connection string
    present_params = {param.split('=')[0] for param in params}
    
    # Check if all required parameters are present
    return required_params.issubset(present_params)