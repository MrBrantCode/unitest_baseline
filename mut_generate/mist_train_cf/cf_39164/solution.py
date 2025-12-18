"""
QUESTION:
Create a function `extract_license_info(license_text: str) -> dict` that takes a software license text as input and returns a dictionary containing the extracted key-value pairs. The license text follows a specific format, with each line starting with a "#" symbol followed by a space and then the key-value pair separated by a colon. The keys are in uppercase and the values are in sentence case. If a key is not present in the license text, it should not be included in the output dictionary.
"""

def extract_license_info(license_text: str) -> dict:
    extracted_info = {}
    lines = license_text.split("\n")
    for line in lines:
        if line.startswith("# "):
            key_value = line[2:].split(": ")
            key = key_value[0].strip()
            value = key_value[1].strip()
            extracted_info[key] = value
    return extracted_info