"""
QUESTION:
Write a function `generate_dropdown` that takes a list of options as input and returns HTML code for a dropdown selection list with the following requirements: 

- Options are displayed in alphabetical order.
- The first option in the list is selected by default.
- The text color of the selected option is red.
- The dropdown has a placeholder text of "Select an option" when no option is selected.
- The dropdown has a maximum visible option count of 3; if there are more than 3 options, a scrollbar appears to view all options.
"""

def generate_dropdown(options):
    """
    Generate HTML code for a dropdown selection list.

    Args:
    options (list): A list of options for the dropdown.

    Returns:
    str: HTML code for the dropdown selection list.
    """
    sorted_options = sorted(options)
    dropdown_html = '<select size="3" style="overflow-y:auto;">'
    dropdown_html += '<option value="" disabled selected style="display:none;">Select an option</option>'
    for option in sorted_options:
        if option == sorted_options[0]:
            dropdown_html += f'<option value="{option}" selected style="color:red;">{option}</option>'
        else:
            dropdown_html += f'<option value="{option}">{option}</option>'
    dropdown_html += '</select>'
    return dropdown_html