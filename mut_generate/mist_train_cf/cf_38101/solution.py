"""
QUESTION:
Implement a function `process_text` that takes two inputs: a string `input_text` and a dictionary `context`. The `context` dictionary has a key "declared" which maps to a list of declared words. Replace each declared word in the `input_text` with its corresponding value from the `context`. If no corresponding value exists in the `context`, use the word itself as the replacement value. The function should remove leading and trailing whitespace from the `input_text` and return the modified text.
"""

import re

def process_text(input_text, context):
    input_text = input_text.strip()
    lookup = {name: name for name in context["declared"]}

    for name in context["declared"]:
        lookup[name] = context.get(name, name)

    modified_text = re.sub(r'\b(' + '|'.join(lookup.keys()) + r')\b', lambda x: lookup[x.group()], input_text)

    return modified_text