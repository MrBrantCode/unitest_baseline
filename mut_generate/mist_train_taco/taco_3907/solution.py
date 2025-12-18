"""
QUESTION:
Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones. For example, given `["apple","rottenBanana","apple"]` the replaced array should be `["apple","banana","apple"]`. Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the rotten fruits are replaced by good ones. 

### Notes

- If the array is null/nil/None or empty you should return empty array (`[]`).
- The rotten fruit name will be in this camelcase (`rottenFruit`).
- The returned array should be in lowercase.
"""

def replace_rotten_fruits(bag_of_fruits):
    """
    Replaces all rotten fruits in the given list with fresh ones and converts all fruits to lowercase.

    Parameters:
    - bag_of_fruits (list of str): A list of strings representing fruits, which may include rotten fruits.

    Returns:
    - list of str: A list of strings where all rotten fruits are replaced with fresh ones and all strings are in lowercase.
    """
    if not bag_of_fruits:
        return []
    
    return [fruit.replace('rotten', '').lower() for fruit in bag_of_fruits]