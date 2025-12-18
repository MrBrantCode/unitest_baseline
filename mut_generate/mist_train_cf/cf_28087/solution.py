"""
QUESTION:
Implement the `process_chunks` function to process a list of chunks and group them based on a specific key. Each chunk is a tuple containing a list of data and a key. The function should concatenate the data of the chunks within each group and return a dictionary where the keys are the unique keys from the chunks and the values are the concatenated data of the corresponding groups. The input list of chunks is assumed to be sorted based on the key.
"""

from itertools import groupby, chain

def process_chunks(chunks):
    grouped_data = {}
    for key, group in groupby(chunks, key=lambda x: x[1]):
        data = list(chain.from_iterable(chunk[0] for chunk in group))
        grouped_data[key] = data
    return grouped_data