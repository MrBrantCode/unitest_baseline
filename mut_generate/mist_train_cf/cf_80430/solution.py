"""
QUESTION:
Create a function called `fetch_info()` that takes a dictionary and a key as arguments. The function should navigate through the dictionary and return the value associated with the given key. If the key is not present in the dictionary, the function should return a message indicating that no data was found for the key. The function should handle potential issues like wrong keys or missing data.
"""

def fetch_info(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return f"No data found for key: {key}"