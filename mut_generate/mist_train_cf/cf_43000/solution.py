"""
QUESTION:
Write a function `extract_diagnostic_info(code_snippet)` that takes a string of diagnostic comments as input and returns a dictionary with the extracted diagnostic information for both 64-bit and 32-bit architectures. The dictionary should have the following structure:
- Keys: "64-bit" and "32-bit"
- Values: Dictionaries with the following keys: "Instance pointer", "Type reference", and "Type info"

The function should extract the corresponding values from the input string based on the patterns in the comments. The "Instance pointer" should be extracted from comments containing "Instance pointer in child address space:", the "Type reference" should be extracted from comments containing "(class", and the "Type info" should be extracted from comments containing "(reference kind=" or be an empty string if not found.
"""

import re

def extract_diagnostic_info(code_snippet):
    diagnostic_info = {
        "64-bit": {},
        "32-bit": {}
    }

    pattern = r'// CHECK-(\d+): (.+)'

    matches = re.findall(pattern, code_snippet)
    for match in matches:
        arch, info = match
        arch = "64-bit" if arch == "64" else "32-bit"
        if "Instance pointer in child address space:" in info:
            diagnostic_info[arch]["Instance pointer"] = re.search(r'0x([0-9a-fA-F]+)', info).group(0)
        elif "(class" in info:
            diagnostic_info[arch]["Type reference"] = re.search(r'\(class (.+)\)', info).group(1)
        elif "(reference kind=" in info:
            diagnostic_info[arch]["Type info"] = re.search(r'\(reference kind=(\w+) refcounting=(\w+)\)', info).group(0)
        else:
            diagnostic_info[arch]["Type info"] = ""

    return diagnostic_info