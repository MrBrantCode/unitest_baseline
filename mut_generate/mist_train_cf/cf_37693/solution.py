"""
QUESTION:
Construct a filename from a string template using the provided mapping of values. Implement the `safe_format_file` function to extract values from the file name or path, and safely format a new filename using the `string.Template` class. If a default mapping is provided in the `mapping` dictionary under the key 'def_mapping', update the `mapping` with the default values from the `default_format_mapping` function. Return the safely formatted filename.
"""

import string

def safe_format_file(s, mapping, fpath):
    """
    Construct a filename from a string template.

    Extract values from the file name / path and use them to safely format a new filename.
    """
    t = string.Template(s)
    if 'def_mapping' in mapping:
        mapping = {**default_format_mapping(), **mapping}
    return t.safe_substitute(mapping)

def default_format_mapping():
    """
    Return a default mapping of values.
    """
    return {'default_key1': 'default_value1', 'default_key2': 'default_value2'}