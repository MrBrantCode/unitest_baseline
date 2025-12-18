"""
QUESTION:
Create a function called `DEPENDS_append` that allows linking an executable from recipe B with a shared library (libxyz.so) from recipe A, considering that A indirectly depends on B through another recipe C. Ensure the solution accommodates the constraint that the shared library does not need to be physically present during the compilation of the executable but must be available at runtime.
"""

def DEPENDS_append(recipe_name):
    """
    Appends the given recipe name to the DEPENDS variable, making it dependent on the provided recipe.

    Args:
        recipe_name (str): The name of the recipe to depend on.
    """
    return f"DEPENDS_append = ' {recipe_name}'"