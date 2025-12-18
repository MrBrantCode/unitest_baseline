"""
QUESTION:
Implement a function `process_form` that takes in three parameters: `col2`, `checkbox_dict`, and `checked`. The function should return a dictionary containing key-value pairs for checked checkboxes, a dictionary containing key-value pairs for text fields, and a tuple containing the name of the widget and a dictionary of checked key-value pairs.

- The `col2` parameter is a list of text strings.
- The `checkbox_dict` parameter is a dictionary of key-value pairs.
- The `checked` parameter is a list of key names that will be checked.

The function should return a tuple of three values:
- A dictionary where each key is a checked checkbox name and the value is `True`.
- A dictionary where each key is a text field name in the format 'widgetname:checked-{key}' and the value is the corresponding text string from `col2`.
- A tuple containing the string 'widgetname' and a dictionary of checked key-value pairs.

Note: The order of key-value pairs in the dictionaries is not guaranteed if the Python version is less than 3.7.
"""

from typing import List, Union, Dict, Tuple

def process_form(col2: List[str], checkbox_dict: Union[Dict], checked: List[str]) -> Tuple[Dict[str, bool], Dict[str, str], Tuple[str, Dict[str, bool]]]:
    checkbox_values = {key: True for key in checked}
    text_values = {f'widgetname:checked-{key}': value for key, value in zip(checked, col2)}
    widget_checked = ('widgetname', checkbox_values)
    return checkbox_values, text_values, widget_checked