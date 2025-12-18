"""
QUESTION:
Implement a class `CitationProcessor` with the following private methods:

- `_cleanup`: This method should delete the directory specified by the `unzipped_directory` attribute and log the action using `logging.info`.
- `_extract_raw_citation`: This method should take a line of text as input, unescape any HTML entities using `html.unescape`, extract the JSON data within the line (between the first occurrence of "{" and the first occurrence of " </w:instrText>"), and return the parsed JSON object using `json.loads`.
- `_extract_citation`: This method should take a line of text as input, extract the raw citation data using `_extract_raw_citation`, extract the first citation item from the raw citation data, modify the item's ID by prefixing it with "Item-", and return the modified item.
"""

import html
import json

def extract_citation(line):
    line = html.unescape(line)
    js = line[line.find("{"):line.find(" </w:instrText>")]
    raw_citation = json.loads(js)
    item_data = raw_citation["citationItems"][0]["itemData"]
    item_data["id"] = "Item-{}".format(item_data["id"])
    return item_data