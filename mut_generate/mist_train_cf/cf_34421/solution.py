"""
QUESTION:
Write a function called `filter_supported_extensions` that takes a list of file extensions as input and returns a filtered list containing only the supported file extensions. The function should check for the availability of certain modules and functions. The supported file extensions are `.py`, `.csv`, `.txt`, and `.h5`. The input list of file extensions may contain uppercase and lowercase extensions. The function should perform case-insensitive comparison when checking the extensions.

The function signature should be:
```python
def filter_supported_extensions(extensions: list) -> list:
```
"""

def filter_supported_extensions(extensions: list) -> list:
    supported_extensions = ['.py', '.csv', '.txt', '.h5']
    return [ext.lower() for ext in extensions if ext.lower() in supported_extensions]