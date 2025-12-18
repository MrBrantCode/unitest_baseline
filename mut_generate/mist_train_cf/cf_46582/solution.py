"""
QUESTION:
Create a function `process_sequence` that takes a multi-tiered numerical sequence as input and returns a dictionary. The dictionary should have unique numbers from the sequence as keys and their corresponding frequency within the sequence as values. The function should be able to handle nested lists of arbitrary depth.
"""

def process_sequence(sequence):
    """Process a multi-tiered complex sequence, returning a dictionary with elements as keys and their frequency as values"""
    def flat_list(nested_list):
        """Flatten a nested list"""
        nested_flatten_list = []
        for i in nested_list:
            if isinstance(i, list):
                nested_flatten_list += flat_list(i)
            else:
                nested_flatten_list.append(i)
        return nested_flatten_list

    def count_elements(sequence):
        """Count the elements in a list"""
        element_counts = {}
        for i in sequence:
            if i in element_counts:
                element_counts[i] += 1
            else:
                element_counts[i] = 1
        return element_counts

    flat_sequence = flat_list(sequence)
    return count_elements(flat_sequence)