"""
QUESTION:
Create a function called `generate_ui` that takes a CSV file as input and returns a string representing a simplified user interface based on the fields in the CSV file. The function should be able to handle any number of fields and generate a corresponding text field for each one. The output string should be a formatted string with each field on a new line, and a submit button at the end. The function should not actually read from the CSV file or handle any UI functionality, but rather provide a simplified representation of what the interface might look like.
"""

def generate_ui(fields):
    """
    Generates a simplified user interface based on the fields provided.

    Args:
        fields (list): A list of field names.

    Returns:
        str: A string representing the user interface.
    """
    ui = ""
    for field in fields:
        ui += f"| {field}:          [  Text Field   ]  |\n"
    ui += "|                                   |\n"
    ui += "|          [Submit Button]          |\n"
    return ui

# Example usage:
fields = ["ID", "Name", "Email", "Phone"]
print(generate_ui(fields))