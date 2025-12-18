"""
QUESTION:
Implement the `create_manager` function, which takes a `token` as input and returns an object of type `Manager`, using the `get_token` function to verify the provided token. The `create_manager` function signature is as follows:
```python
def create_manager(token: str) -> Manager:
```
"""

class Manager:
    pass

def get_token(token: str) -> str:
    # Simulated function to retrieve token
    return "actual-token"

def create_manager(token: str) -> Manager:
    # Simulated function to create Manager object using token
    if get_token(token) == token:
        return Manager()
    else:
        return None