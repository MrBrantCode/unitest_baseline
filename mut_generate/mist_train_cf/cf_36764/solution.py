"""
QUESTION:
Write a function `parse_metadata(markdown: str) -> dict` that takes a markdown text as input and returns a dictionary containing the extracted metadata. The function should adhere to the following rules:
- The metadata is enclosed within a pair of triple dashes (`---`) at the beginning of the markdown text and ends with another pair of triple dashes.
- Each key-value pair is specified on a separate line in the format `key: value`.
- The keys and values are separated by a colon followed by a space (`: `).
- The function should return a dictionary where the keys are the metadata keys and the values are the corresponding metadata values.
- If the input markdown does not contain metadata, the function should return an empty dictionary.
"""

def parse_metadata(markdown: str) -> dict:
    metadata = {}
    if markdown.startswith('---'):
        end_index = markdown.find('---', 3)
        if end_index != -1:
            metadata_text = markdown[3:end_index].strip()
            lines = metadata_text.split('\n')
            for line in lines:
                key_value = line.split(': ', 1)
                if len(key_value) == 2:
                    key, value = key_value
                    metadata[key.strip()] = value.strip()
    return metadata