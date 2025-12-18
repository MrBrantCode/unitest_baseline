"""
QUESTION:
Implement a function `get_file_type` that takes a file name as input and returns its corresponding file type based on its extension. The file types and their corresponding extensions are stored in a dictionary, and the function should return "Unknown" if the extension is not found in the dictionary. The function should handle file names with extensions in any case (lowercase, uppercase, or mixed case) by treating them as lowercase. The dictionary of file types and their corresponding extensions is:
```python
{
    "pdf": "application/pdf",
    "zip": "application/zip",
    "txt": "text/plain",
    "jpg": "image/jpeg",
    "png": "image/png"
}
```
"""

def get_file_type(file_name: str) -> str:
    file_extension = file_name.split(".")[-1].lower()
    file_types = {
        "pdf": "application/pdf",
        "zip": "application/zip",
        "txt": "text/plain",
        "jpg": "image/jpeg",
        "png": "image/png"
    }
    return file_types.get(file_extension, "Unknown")