"""
QUESTION:
Implement a method `calculate_total_size` that calculates the total size of a given folder and all its subfolders and files. The method should take a `Folder` instance as input and return the total size in bytes. The `Folder` model has a `size` attribute representing the size of the folder in bytes and a `parent` attribute representing the parent folder. The method should recursively include the sizes of all subfolders and files within the given folder.
"""

def calculate_total_size(folder):
    """
    Recursively calculates the total size of a given folder and all its subfolders and files.

    Args:
        folder (Folder): The folder instance to calculate the size for.

    Returns:
        int: The total size in bytes of the folder and its subfolders and files.
    """
    total_size = folder.size
    # Assuming 'folder.subfolders' is a list of subfolders
    for subfolder in folder.subfolders:
        total_size += calculate_total_size(subfolder)
    return total_size