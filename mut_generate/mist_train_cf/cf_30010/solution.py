"""
QUESTION:
Write a function `process_files` that takes a list of file names as input, processes the list based on the following rules, and returns a list of included file names:
- Remove any leading or trailing whitespace from each file name.
- Exclude any file name that contains the word "temp".
- Include any file name that ends with ".txt".
- Include any file name that starts with "data_" and has a length greater than 10 characters.
"""

def process_files(all_files):
    included_files = []
    for f in all_files:
        f = f.strip()
        if "temp" in f:
            continue
        if f.endswith(".txt") or (f.startswith("data_") and len(f) > 10):
            included_files.append(f)
    return included_files