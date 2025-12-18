"""
QUESTION:
Write a method that will search an array of strings for all strings that contain another string, ignoring capitalization. Then return an array of the found strings. 

The method takes two parameters, the query string and the array of strings to search, and returns an array. 

If the string isn't contained in any of the strings in the array, the method returns an array containing a single string: "Empty" (or `Nothing` in Haskell, or "None" in Python and C)

### Examples
If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"], the method should return ["home", "Mercury"].
"""

def search_strings_with_query(query: str, seq: list[str]) -> list[str]:
    """
    Searches an array of strings for all strings that contain another string, ignoring capitalization.

    Parameters:
    - query (str): The string to search for.
    - seq (list[str]): The array of strings to search within.

    Returns:
    - list[str]: An array of strings that contain the `query` string, ignoring capitalization.
                 If no strings contain the `query`, returns an array containing the string "None".
    """
    return [x for x in seq if query.lower() in x.lower()] or ["None"]