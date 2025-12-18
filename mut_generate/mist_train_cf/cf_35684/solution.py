"""
QUESTION:
Implement the `process_genetic_variant` function that takes in a dictionary representing a genetic variant with a 'genotype_calls' key containing a dictionary of genotype calls, and returns a formatted string with the genotype calls separated by commas, sorted by identifier. The function should handle cases where the 'genotype_calls' key is missing or empty.
"""

def process_genetic_variant(variant: dict) -> str:
    genotype_calls = variant.get('genotype_calls', {})
    return ','.join([genotype_calls[key] for key in sorted(genotype_calls.keys())])