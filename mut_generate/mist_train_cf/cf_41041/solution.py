"""
QUESTION:
Write a function `handleStorageException` that takes a `StorageException` object as a parameter. The `StorageException` object has a property `RequestInformation` containing the HTTP status code as an integer. If the HTTP status code is 404, the function should return the string "Resource not found". If the status code is not 404, the function should return the string "Other storage exception".
"""

def handleStorageException(e):
    if e.RequestInformation.HttpStatusCode == 404:
        return "Resource not found"
    else:
        return "Other storage exception"