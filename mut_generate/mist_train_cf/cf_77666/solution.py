"""
QUESTION:
Implement a function `bloom_filter_or_skip_list` to determine whether to use a Bloom filter or a skip list in a given scenario. The function should take two parameters: `data_size` representing the number of elements in the dataset and `operation` representing the type of operation to be performed. The `operation` parameter can be either 'existence_check' or 'ordered_sequence'. If `operation` is 'existence_check' and `data_size` is greater than 10,000, return 'Bloom filter'. If `operation` is 'ordered_sequence', return 'Skip list'. Otherwise, return 'Skip list'.
"""

def bloom_filter_or_skip_list(data_size, operation):
    """
    Determine whether to use a Bloom filter or a skip list in a given scenario.

    Args:
    data_size (int): The number of elements in the dataset.
    operation (str): The type of operation to be performed. It can be either 'existence_check' or 'ordered_sequence'.

    Returns:
    str: 'Bloom filter' or 'Skip list' based on the given conditions.
    """
    
    # If operation is 'existence_check' and data_size is greater than 10,000, return 'Bloom filter'
    if operation == 'existence_check' and data_size > 10000:
        return 'Bloom filter'
    
    # If operation is 'ordered_sequence', return 'Skip list'
    elif operation == 'ordered_sequence':
        return 'Skip list'
    
    # In all other cases, return 'Skip list'
    else:
        return 'Skip list'