"""
QUESTION:
Create a function `generate_laptop_id` that takes a manufacturer name, screen size, and processor type as input and returns a unique identifier. The identifier should be a string consisting of the manufacturer name (truncated to 6 characters), screen size (rounded to one decimal place), and processor type (truncated to 4 characters), separated by underscores.
"""

def generate_laptop_id(manufacturer, screen_size, processor_type):
    """
    Generate a unique identifier for a laptop.
    
    Parameters:
    manufacturer (str): The manufacturer name of the laptop.
    screen_size (float): The screen size of the laptop.
    processor_type (str): The processor type of the laptop.
    
    Returns:
    str: A unique identifier in the format "manufacturer_screen_size_processor_type".
    """
    return f"{manufacturer[:6]}_{round(screen_size, 1)}_{processor_type[:4]}"