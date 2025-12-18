"""
QUESTION:
Implement the `compile_inverted_index` function, which generates an inverted index for a collection of documents. The function should take a `block_size_limit` parameter as input, representing the maximum number of documents to be processed at a time. The function should process the documents in blocks of size `block_size_limit`, and generate an inverted index that maps each unique word in the documents to the list of document IDs in which it appears. The preprocessing involves tokenizing the text, converting it to lowercase, and removing any non-alphanumeric characters. The function should return the inverted index as a dictionary.
"""

import re
from collections import defaultdict

def compile_inverted_index(documents, block_size_limit):
    """ Generate inverted index for a collection of documents """
    inverted_index = defaultdict(list)

    for i in range(0, len(documents), block_size_limit):
        block_documents = documents[i:i + block_size_limit]
        for doc_id, doc in enumerate(block_documents, start=i):
            words = re.findall(r'\b\w+\b', re.sub(r'\W+', ' ', doc).lower())
            for word in set(words):  
                inverted_index[word].append(doc_id)

    return inverted_index