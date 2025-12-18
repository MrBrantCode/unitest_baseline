"""
QUESTION:
Implement a function `count_uri_prefixes(synonymLabelURIs)` that takes a set of URI strings as input and returns a dictionary containing the count of unique ontologies for each URI prefix. The URI prefix is defined as the part of the URI before the first '#' character. The function should return a dictionary where the keys are the URI prefixes and the values are the count of unique ontologies for each prefix.
"""

def count_uri_prefixes(synonymLabelURIs):
    uri_prefix_count = {}
    for uri in synonymLabelURIs:
        prefix = uri.split('#')[0]
        if prefix in uri_prefix_count:
            uri_prefix_count[prefix] += 1
        else:
            uri_prefix_count[prefix] = 1
    return uri_prefix_count