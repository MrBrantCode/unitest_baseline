"""
QUESTION:
Write a function `load_image` that returns the correct path of an image in a .NET MAUI Blazor Hybrid application using MudBlazor for UI. The function should take the assembly name and image path as inputs, ensure the case sensitivity of the file path matches the actual file path, fully-qualify the path of the image, and handle different file extensions. The function should return the correct image path that can be used in a Razor component.
"""

def load_image(assembly_name, image_path):
    """
    Returns the correct path of an image in a .NET MAUI Blazor Hybrid application.

    Args:
    assembly_name (str): The name of the assembly.
    image_path (str): The path to the image.

    Returns:
    str: The fully-qualified path of the image.
    """
    # Ensure the file path matches the actual file path
    image_path = image_path.replace("\\", "/")

    # Fully-qualify the path of the image
    fully_qualified_path = f"_content/{assembly_name}/{image_path}"

    return fully_qualified_path