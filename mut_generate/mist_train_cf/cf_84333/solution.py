"""
QUESTION:
Design a function called `identify_datatype` that takes one parameter and returns its datatype as a string. The function should map the raw datatype names to nicer names. If the datatype is unknown, return 'Unknown'.
"""

def identify_datatype(value):
    datatype = type(value).__name__
    
    categories = {
        'int': 'Integer',
        'float': 'Float',
        'str': 'String',
        'bool': 'Boolean',
        'tuple': 'Tuple',
        'list': 'List',
        'dict': 'Dictionary',
        'set': 'Set',
        'NoneType': 'None',
    }

    return categories.get(datatype, 'Unknown')