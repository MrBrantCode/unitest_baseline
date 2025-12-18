"""
QUESTION:
Create a function `display_vegetable_info` that takes a list of vegetables with their corresponding colors and images, and a list of alphabets and languages as input. The function should return a webpage that displays buttons labeled with different vegetable names. When a button is clicked, the background color of the webpage should change to a color associated with that vegetable, and an image of that particular vegetable should be displayed. The webpage should also include a dropdown menu to filter the vegetables based on the starting alphabet and a dropdown menu to switch between languages. The application should handle errors gracefully and optimize API calls for performance and speed.
"""

def display_vegetable_info(vegetables, alphabets, languages):
    """
    This function generates a webpage displaying buttons labeled with different vegetable names.
    When a button is clicked, the background color of the webpage changes to a color associated with that vegetable,
    and an image of that particular vegetable is displayed. The webpage also includes a dropdown menu to filter
    the vegetables based on the starting alphabet and a dropdown menu to switch between languages.

    Args:
        vegetables (list): A list of dictionaries containing vegetable information (name, color, image).
        alphabets (list): A list of alphabets for filtering vegetables.
        languages (list): A list of languages for switching between languages.

    Returns:
        A webpage with interactive features.
    """
    # Create a dictionary to store vegetable information
    vegetable_info = {}
    for vegetable in vegetables:
        vegetable_info[vegetable['name']] = {'color': vegetable['color'], 'image': vegetable['image']}

    # Create a dictionary to store alphabet and language options
    options = {'alphabets': alphabets, 'languages': languages}

    # Generate HTML content for the webpage
    html_content = generate_html(vegetable_info, options)

    # Return the HTML content
    return html_content


def generate_html(vegetable_info, options):
    # Create HTML skeleton
    html = '<html><body>'

    # Create buttons for each vegetable
    for vegetable, info in vegetable_info.items():
        html += f'<button onclick="changeBackgroundAndImage(\'{info["color"]}\', \'{info["image"]}\')"> {vegetable} </button>'

    # Create dropdown menu for alphabets
    html += '<select id="alphabet-dropdown">'
    for alphabet in options['alphabets']:
        html += f'<option value="{alphabet}">{alphabet}</option>'
    html += '</select>'

    # Create dropdown menu for languages
    html += '<select id="language-dropdown">'
    for language in options['languages']:
        html += f'<option value="{language}">{language}</option>'
    html += '</select>'

    # Add image tag
    html += '<img id="vegetable-image" src="">'

    # Add JavaScript code for button click event
    html += '<script> function changeBackgroundAndImage(color, image) { document.body.style.background = color; document.getElementById("vegetable-image").src = image; } </script>'

    # Close HTML tags
    html += '</body></html>'

    return html