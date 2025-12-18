"""
QUESTION:
Implement the `parse_bro_log_header` function, which takes a string representing a Bro log header section as input. The header section consists of two lines: `#fields` followed by field names separated by tabs and `#types` followed by corresponding data types separated by tabs. Return a dictionary mapping field names to their data types.
"""

def parse_bro_log_header(header_section):
    fields = header_section.split('#fields')[1].split('#types')[0].strip().split('\t')
    types = header_section.split('#types')[1].strip().split('\t')
    return dict(zip(fields, types))