"""
QUESTION:
Implement a function `deserialize_edges` that takes a list of serialized edges as input. Each edge is represented as a string in the format `source_id,DESTINATION,weight`. The function should return a dictionary representing the deserialized edges. The keys of the dictionary should be the source identifiers, and the values should be lists of tuples representing the destination identifier and the weight.
"""

def deserialize_edges(serialized_edges):
    deserialized_edges = {}
    for edge in serialized_edges:
        source_id, destination, weight = edge.split(',')
        if source_id not in deserialized_edges:
            deserialized_edges[source_id] = []
        deserialized_edges[source_id].append((destination, int(weight)))
    return deserialized_edges