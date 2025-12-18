"""
QUESTION:
Write a function `analyze_gene_fragments` that takes a list of integers representing gene fragment lengths and a positive integer threshold as input. Return a tuple containing the average length of the gene fragments, the number of fragments that exceed the threshold length, and the index of the longest gene fragment in the list.
"""

import numpy

def analyze_gene_fragments(gene_fragments, threshold):
    average_length = sum(gene_fragments) / len(gene_fragments)
    count_exceeding_threshold = sum(1 for length in gene_fragments if length > threshold)
    longest_fragment_index = gene_fragments.index(max(gene_fragments))
    return (average_length, count_exceeding_threshold, longest_fragment_index)