"""
QUESTION:
Create a function `create_wordpress_theme` that generates a basic Wordpress theme. The theme should include a style.css file with CSS styles, an index.php file for the basic HTML layout, and a screenshot.png image for display in the WordPress dashboard. Optional files may include a page.php template, functions.php, and scripts.php. The function should not actually create files, but rather describe the steps to create a basic Wordpress theme.
"""

def create_wordpress_theme(theme_name):
    """
    This function generates a basic Wordpress theme.
    
    Parameters:
    theme_name (str): The name of the theme folder.
    
    Returns:
    str: A description of the steps to create a basic Wordpress theme.
    """
    
    # Create a new folder for your theme, name it as per the theme_name parameter.
    theme_folder = theme_name
    
    # Create a style.css file in your theme folder. Add all the CSS styles as required to make your theme looks as desired.
    style_css = f"{theme_folder}/style.css"
    
    # Create an index.php file in your theme folder, and add the code to create a basic layout of your theme in HTML.
    index_php = f"{theme_folder}/index.php"
    
    # Create any other files you may need, such as a template file (example: page.php), functions.php and scripts.php, in order to make your theme fully functional.
    page_php = f"{theme_folder}/page.php"
    functions_php = f"{theme_folder}/functions.php"
    scripts_php = f"{theme_folder}/scripts.php"
    
    # Add code to your functions.php file to add different features to your theme.
    
    # Create a screenshot.png image of your theme inside your theme folder, to show in the WordPress dashboard.
    screenshot_png = f"{theme_folder}/screenshot.png"
    
    # Zip your theme folder and upload it to WordPress from the “Appearance” menu.
    return f"Create the following files in the {theme_name} folder: {style_css}, {index_php}, {page_php}, {functions_php}, {scripts_php}, {screenshot_png}. Then, zip the {theme_name} folder and upload it to WordPress from the “Appearance” menu."