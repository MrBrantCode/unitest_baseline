"""
QUESTION:
Create a function named `create_metadata` that generates and returns a string of common metadata elements for a given web page, including title, description, keywords, author, and charset. The function should take the following parameters: `title`, `description`, `keywords` (a list of strings), `author`, and `charset`. The function should also include the `viewport` and `robots` metadata elements with default values 'width=device-width, initial-scale=1.0' and 'index, follow', respectively.
"""

def create_metadata(title, description, keywords, author, charset):
    """
    Generate and return a string of common metadata elements for a given web page.

    Parameters:
    title (str): The title of the web page.
    description (str): A summary of the web content.
    keywords (list): A list of descriptive words for the web page.
    author (str): The name of the author of the webpage.
    charset (str): The character encoding for the web page.

    Returns:
    str: A string of common metadata elements.
    """

    metadata = "<head>\n"
    
    # Add title metadata
    metadata += "    <!-- Title -->\n"
    metadata += f"    <title>{title}</title>\n\n"

    # Add description metadata
    metadata += "    <!-- Description -->\n"
    metadata += f"    <meta name=\"description\" content=\"{description}\">\n\n"

    # Add keywords metadata
    metadata += "    <!-- Keywords -->\n"
    metadata += f"    <meta name=\"keywords\" content=\"{', '.join(keywords)}\">\n\n"

    # Add author metadata
    metadata += "    <!-- Author -->\n"
    metadata += f"    <meta name=\"author\" content=\"{author}\">\n\n"

    # Add charset metadata
    metadata += "    <!-- Charset -->\n"
    metadata += f"    <meta charset=\"{charset}\">\n\n"

    # Add viewport metadata
    metadata += "    <!-- Viewport -->\n"
    metadata += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\n"

    # Add robots metadata
    metadata += "    <!-- Robots -->\n"
    metadata += "    <meta name=\"robots\" content=\"index, follow\">\n"

    metadata += "</head>"
    
    return metadata