"""
QUESTION:
Write a function `parseHTMLForm(html)` that takes a string `html` representing an HTML form as input. The function should parse the form and return a dictionary containing the form's attributes and a list of its input elements. The function should handle HTML forms with any number of input elements, including `<input>`, `<select>`, and `<textarea>` tags, and any attributes associated with these elements. 

The function should return a dictionary with the following structure:
```python
{
    "form_attributes": {
        "action": "url",
        "method": "get/post",
        # other form attributes
    },
    "input_elements": [
        {
            "tag": "input/select/textarea",
            "attributes": {
                "name": "input_name",
                "type": "text/checkbox/submit/etc.",
                # other attributes
            }
        },
        # other input elements
    ]
}
```
There are no restrictions on the input HTML, but the function should be able to handle any valid HTML form.
"""

import re

def parseHTMLForm(html):
    form_data = {"form_attributes": {}, "input_elements": []}

    form_match = re.search(r'<form\s+([^>]+)>', html)
    if form_match:
        attributes = form_match.group(1)
        attribute_dict = {}
        attribute_pairs = re.findall(r'(\w+)="([^"]+)"', attributes)
        for pair in attribute_pairs:
            attribute_dict[pair[0]] = pair[1]
        form_data["form_attributes"] = attribute_dict

    input_matches = re.finditer(r'<(input|select|textarea)\s+([^>]+)>', html)
    for match in input_matches:
        tag = match.group(1)
        attributes = match.group(2)
        attribute_dict = {}
        attribute_pairs = re.findall(r'(\w+)="([^"]+)"', attributes)
        for pair in attribute_pairs:
            attribute_dict[pair[0]] = pair[1]
        form_data["input_elements"].append({"tag": tag, "attributes": attribute_dict})

    return form_data