"""
QUESTION:
Implement a function `custom_sort` that takes a list of documents from a MongoDB collection as input, where each document contains multiple nested fields. The function should sort the documents in ascending order based on a specific nested field, for example "nested_field.nested_subfield", without using the built-in sort function provided by MongoDB.
"""

def custom_sort(documents, field):
    """
    Sorts a list of documents in ascending order based on a specific nested field.

    Args:
    documents (list): A list of documents from a MongoDB collection.
    field (str): A string representing the nested field to sort by, using dot notation (e.g., "nested_field.nested_subfield").

    Returns:
    list: The sorted list of documents.
    """
    def get_nested_field_value(document, field):
        """Helper function to retrieve the value of a nested field in a document."""
        nested_fields = field.split('.')
        value = document
        for nested_field in nested_fields:
            value = value.get(nested_field, {})
        return value

    def merge_sort(documents, field):
        """Recursive merge sort algorithm implementation."""
        if len(documents) <= 1:
            return documents
        mid = len(documents) // 2
        left_half = merge_sort(documents[:mid], field)
        right_half = merge_sort(documents[mid:], field)
        return merge(left_half, right_half, field)

    def merge(left, right, field):
        """Merge two sorted lists into one."""
        merged = []
        left_index = 0
        right_index = 0
        while left_index < len(left) and right_index < len(right):
            if get_nested_field_value(left[left_index], field) <= get_nested_field_value(right[right_index], field):
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        merged.extend(left[left_index:])
        merged.extend(right[right_index:])
        return merged

    return merge_sort(documents, field)