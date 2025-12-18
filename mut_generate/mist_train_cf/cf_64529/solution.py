"""
QUESTION:
Write a function called `compress_textual_data` that takes a list of strings as input, compresses the data by replacing words with unique identifiers, and returns the compressed data along with the mapping of words to identifiers. The function should be efficient in terms of storage capacity reduction, especially when there is redundancy in the input data.
"""

def compress_textual_data(data):
    # Extract unique tokens (words) from the input data
    tokens = set([word for sentence in data for word in sentence.split(" ")])

    # Create a mapping of words to unique identifiers
    token_map = {token: i for i, token in enumerate(tokens)}

    # Compress the data by replacing words with their identifiers
    compressed_data = [[token_map[word] for word in sentence.split(" ")] for sentence in data]

    # Return the compressed data along with the mapping of words to identifiers
    return compressed_data, token_map