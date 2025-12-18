"""
QUESTION:
Implement a media query function `apply_media_query` that takes media type and media query expression as parameters, and returns a corresponding CSS stylesheet when the condition is true. The function should handle different screen sizes and adapt a web page accordingly.
"""

def apply_media_query(media_type, media_query_expression, css_stylesheet):
    """
    This function applies a media query based on the given media type and media query expression.
    
    Args:
        media_type (str): The type of media (e.g., screen, print, all).
        media_query_expression (str): The media query expression (e.g., min-width: 768px, max-width: 1024px).
        css_stylesheet (str): The CSS stylesheet to be applied when the media query condition is true.
    
    Returns:
        str: The corresponding CSS stylesheet when the condition is true.
    """
    return f"@media {media_type} and ({media_query_expression}) {{\n{css_stylesheet}\n}}"