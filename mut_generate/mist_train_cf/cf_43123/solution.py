"""
QUESTION:
Create a Python function `process_arguments` that takes a list of strings representing command-line arguments as input. The function should parse the list to extract accession numbers following the `-number` flag and reference numbers following the `-reference` flag. The function should return a tuple containing the accession number and reference number in that order. If an accession number or reference number is not provided, the corresponding value in the tuple should be an empty string.
"""

def process_arguments(args):
    accession_number = ''
    reference_number = ''
    i = 0
    while i < len(args):
        if args[i] == '-number' and i + 1 < len(args):
            accession_number = args[i + 1]
        elif args[i] == '-reference' and i + 1 < len(args):
            reference_number = args[i + 1]
        i += 1
    return (accession_number, reference_number)