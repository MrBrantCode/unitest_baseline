"""
QUESTION:
Create a function named `extract_distinct_elements` that takes a collection of elements as input and returns a list of distinct tuple elements from the collection. The function should ignore non-tuple elements in the collection and consider tuple elements distinct based on their constituent parts, i.e., ('X',7) and ('X',6) are considered distinct. The function should handle potential errors gracefully using exception handling.
"""

def extract_distinct_elements(collection):
    distinct_elements = []
    
    # Iterate over each item in the collection
    for element in collection:
        # Check if the element is a tuple
        if isinstance(element, tuple):
            # Check if the element is not already in the list
            if element not in distinct_elements:
                # Add the element to the list
                distinct_elements.append(element)
                
    return distinct_elements