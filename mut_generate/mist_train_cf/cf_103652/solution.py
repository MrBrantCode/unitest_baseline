"""
QUESTION:
Design a function `format_slug` that formats a given string as a URL slug. The function should remove any special characters and replace spaces with hyphens, with the resulting slug being all lowercase. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def format_slug(string):
    slug = string.lower().replace(" ", "-")
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '<', '>', ',', '.', '/', '?']
    for char in special_chars:
        slug = slug.replace(char, "")
    return slug