"""
QUESTION:
Create a function `process_metadata(metadata: List[str]) -> Dict[str, Union[str, List[str]]]` that takes in a list of metadata strings where each string contains a key-value pair separated by a double colon (::). The function should extract and return the development status, intended audience, and topics related to the project, storing them in a dictionary with keys "Development Status", "Intended Audience", and "Topic". If a key is not present in the metadata, the corresponding value in the dictionary should be an empty string or an empty list.
"""

from typing import List, Dict, Union

def process_metadata(metadata: List[str]) -> Dict[str, Union[str, List[str]]]:
    extracted_info = {
        "Development Status": "",
        "Intended Audience": "",
        "Topic": []
    }

    for line in metadata:
        key_value = line.split("::")
        if len(key_value) == 2:
            key = key_value[0].strip().strip("'")
            value = key_value[1].strip().strip("'")
            if key == "Development Status":
                extracted_info["Development Status"] = value
            elif key == "Intended Audience":
                extracted_info["Intended Audience"] = value
            elif key == "Topic":
                extracted_info["Topic"] = value.split(" :: ")

    return extracted_info