"""
QUESTION:
Implement a function called `to_html` that takes a single argument `value` and returns its HTML representation, supporting the following conversions:
- String: enclosed in `<p>` tags
- Boolean: "Yes" enclosed in `<strong>` tags if `True`, and "No" enclosed in `<em>` tags if `False`
- List: unordered list (`<ul>`) with each item enclosed in `<li>` tags
- Dictionary: definition list (`<dl>`) with each key-value pair enclosed in `<dt>` and `<dd>` tags, respectively
"""

def to_html(value):
    if isinstance(value, str):
        return f'<p>{value}</p>'
    elif isinstance(value, bool):
        return f'<strong>Yes</strong>' if value else f'<em>No</em>'
    elif isinstance(value, list):
        items = ''.join([f'<li>{item}</li>' for item in value])
        return f'<ul>{items}</ul>'
    elif isinstance(value, dict):
        items = ''.join([f'<dt>{key}</dt><dd>{to_html(value[key])}</dd>' for key in value])
        return f'<dl>{items}</dl>'
    else:
        return f'Unsupported type: {type(value)}'