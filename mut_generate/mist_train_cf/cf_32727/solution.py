"""
QUESTION:
Write a function named `parse_ACIItem` that takes an ASN.1 encoded data stream as input and extracts the `id`, `name`, and `value` fields from the `ACIItem` sequence defined as `ACIItem ::= SEQUENCE { id INTEGER, name UTF8String, value OCTET STRING }`. The input is a byte array and the output should be a structured representation of the parsed `ACIItem` data containing the extracted fields.
"""

def parse_ACIItem(encoded_data):
    structure = {
        "id": None,
        "name": None,
        "value": None
    }

    index = 0
    while index < len(encoded_data):
        tag = encoded_data[index]
        length = encoded_data[index + 1]
        value_start = index + 2

        if tag == 0x02:  
            structure["id"] = int.from_bytes(encoded_data[value_start:value_start + length], byteorder='big')
        elif tag == 0x16:  
            structure["name"] = encoded_data[value_start:value_start + length].decode('utf-8')
        elif tag == 0x04:  
            structure["value"] = list(encoded_data[value_start:value_start + length])

        index += length + 2

    return structure