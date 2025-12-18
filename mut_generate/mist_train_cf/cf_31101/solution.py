"""
QUESTION:
Create a function `extract_password` that takes a dictionary `config` and a string `host` as input. The dictionary represents a configuration file where host names and passwords are stored in the format 'hostX': 'host_name' and 'passwordX': '<passwordX>'. The function should return the password associated with the specified host by finding the corresponding 'passwordX' value. If the host or its password is not found, the function should return "Password not found for the specified host."
"""

def extract_password(config: dict, host: str) -> str:
    for key, value in config.items():
        if key.startswith('host') and value == host:
            password_key = 'password' + key[4:]
            if password_key in config:
                return config[password_key].strip('<>')
    return "Password not found for the specified host."