"""
QUESTION:
Create a function `update_ocr_interface` that takes two parameters: 
- `current_interface` (list of strings): The current public interface of the OCR module.
- `new_objects` (list of strings): A list of new objects that need to be added to the public interface.

The function should update the `current_interface` by adding the `new_objects` to it, ensuring that there are no duplicate entries, and then return the updated interface.
"""

def update_ocr_interface(current_interface, new_objects):
    updated_interface = list(set(current_interface + new_objects))
    return updated_interface