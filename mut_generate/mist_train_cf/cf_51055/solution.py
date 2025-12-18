"""
QUESTION:
Write a function `transform_collection(collection)` that takes a collection of text elements as input and returns a distinct unordered group of these elements with no repetition. The function should be case-insensitive and ignore non-alphanumeric characters.
"""

def transform_collection(collection):
    # Initialize an empty set
    distinct_set = set()
    
    # Iterate over each element in the collection
    for element in collection:
        # Remove non-alphanumeric characters and convert to lower case
        cleaned_element = ''.join(e for e in element if e.isalnum()).lower()
        
        # Add the cleaned element to our set
        distinct_set.add(cleaned_element)
    
    # Return the distinct set
    return distinct_set