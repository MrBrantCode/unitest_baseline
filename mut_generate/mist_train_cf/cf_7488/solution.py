"""
QUESTION:
Implement a function `custom_sort_documents` that sorts a list of MongoDB documents based on a specified nested field. The function should handle multi-level deep nested fields and different data types (strings, numbers, dates). The sorting field is dynamic and can change at runtime. The function should have a time complexity better than O(n^2) and handle large datasets efficiently. It should also implement error handling and exception handling to handle potential issues during the sorting process.
"""

def custom_sort_documents(documents, sort_field):
    """
    Sorts a list of MongoDB documents based on a specified nested field.
    
    Args:
        documents (list): A list of MongoDB documents.
        sort_field (str): The field to sort on. Can be a nested field (e.g., 'field1.field2').
    
    Returns:
        list: The sorted list of documents.
    """
    try:
        # Split the sort field into individual fields
        fields = sort_field.split('.')
        
        # Use a lambda function as the key for the sort method
        # This function recursively traverses the document to find the field value
        def get_field_value(document):
            value = document
            for field in fields:
                if field in value:
                    value = value[field]
                else:
                    # If the field does not exist, return a default value to ensure correct sorting
                    return ''
            return value
        
        # Sort the documents based on the specified field
        return sorted(documents, key=get_field_value)
    
    except Exception as e:
        # Handle any exceptions during the sorting process
        print(f"An error occurred: {e}")
        return []