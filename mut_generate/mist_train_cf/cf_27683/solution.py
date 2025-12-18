"""
QUESTION:
Create a function `extractAssemblyInfo` that takes a list of strings representing assembly attributes in the format "key: value". Extract and return the values associated with the keys "Title", "Description", "Company", and "Copyright" as a dictionary. If a key is not present, return "Not Found" for that key.
"""

def extractAssemblyInfo(attributes):
    info = {
        "Title": "Not Found",
        "Description": "Not Found",
        "Company": "Not Found",
        "Copyright": "Not Found"
    }
    for attribute in attributes:
        key, value = attribute.split(": ")
        if key in info:
            info[key] = value
    return info