"""
QUESTION:
Write a function to correctly iterate over an array of objects called "contacts" and display their "link" and "name" properties in a list. The function should check if the "contacts" array is not empty before iterating. Use Embedded JavaScript (EJS) syntax.
"""

def display_contacts(contacts):
    """
    This function displays the 'link' and 'name' properties of each object in the 'contacts' list.
    
    Args:
    contacts (list): A list of objects containing 'link' and 'name' properties.
    
    Returns:
    list: A list of strings containing the formatted 'link' and 'name' properties.
    """
    
    if contacts:  # Check if the 'contacts' list is not empty
        result = []
        for contact in contacts:
            result.append(f"<a href='{contact['link']}'>{contact['name']}</a>")
        return result
    else:
        return []