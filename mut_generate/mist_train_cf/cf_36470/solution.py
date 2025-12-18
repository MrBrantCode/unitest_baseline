"""
QUESTION:
Implement the `has_record_type` function to check if a given record type is supported by the application. The function should take a `record_type` parameter and return `True` if the record type is supported. If the record type is not supported, the function should raise a custom exception with the message "Unsupported record type: <record_type>". The function should adhere to the following requirements:
- Check if the given record type is in the list of supported types: ['individual', 'family', 'event'].
- Raise a custom exception if the record type is not supported.
- Handle the raised exception by providing a user-friendly error message.
"""

class UnsupportedRecordType(Exception):
    pass

def has_record_type(record_type):
    supported_record_types = ['individual', 'family', 'event']
    if record_type in supported_record_types:
        return True
    else:
        raise UnsupportedRecordType(f"Unsupported record type: {record_type}")