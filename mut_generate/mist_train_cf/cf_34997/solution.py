"""
QUESTION:
Create a function named `parse_command_packet` that takes a dictionary representing a JSON object as input and returns a dictionary containing the extracted information. The input dictionary has the following structure: it has a "command" field with "devId", "uid", and "t" sub-fields, a "DP_QUERY_NEW" field with a "hexByte" sub-field and a "command" sub-field with "devId", "uid", and "t" sub-fields, and a "prefix" field containing a hexadecimal string. The output dictionary should contain the "devId", "uid", "t", "hexByte", and "prefix" fields. The function should not take any other arguments besides the input dictionary and should not modify the input dictionary.
"""

def parse_command_packet(command_packet: dict) -> dict:
    extracted_info = {
        "devId": command_packet["command"]["devId"],
        "uid": command_packet["command"]["uid"],
        "t": command_packet["command"]["t"],
        "hexByte": command_packet["DP_QUERY_NEW"]["hexByte"],
        "prefix": command_packet["prefix"]
    }
    return extracted_info