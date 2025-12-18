"""
QUESTION:
Create a function called `generate_ast` to generate an Abstract Syntax Tree (AST) for a custom language. The function should take the source code of the custom language as input. You can use any method such as writing a parser, utilizing language servers, or leveraging third-party libraries. The function should return the generated AST.
"""

def generate_ast(source_code):
    """
    Generate an Abstract Syntax Tree (AST) for a custom language.

    Args:
        source_code (str): The source code of the custom language.

    Returns:
        The generated AST.
    """

    # For simplicity, we'll use the ast module in Python's standard library.
    # This will only work for Python source code.
    import ast

    # Attempt to parse the source code into an AST.
    try:
        # Use the ast.parse function to generate the AST.
        tree = ast.parse(source_code)
    except SyntaxError as e:
        # Handle syntax errors in the source code.
        print(f"Syntax error: {e}")
        return None

    # Return the generated AST.
    return tree