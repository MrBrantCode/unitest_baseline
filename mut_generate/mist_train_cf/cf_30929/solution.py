"""
QUESTION:
Implement the `list_keys` method that returns a list of all the key names stored in the secret manager. The method takes no parameters and should return a list of strings representing the names of the keys. The key names can be retrieved from the `_secret_keys` attribute, which is a list of dictionaries containing the `name` and `value` of each key.
"""

def list_keys(self) -> list:
    key_names = [item['name'] for item in self._secret_keys]
    return key_names