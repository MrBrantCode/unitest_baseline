"""
QUESTION:
Analyze the given context-free grammar: S → ( S ) | x. Determine if the grammar is ambiguous, suitable for top-down parsing, and compatible with bottom-up parsing. Choose the correct option: 

I. The grammar is ambiguous.
II. The grammar is suitable for top-down parsing.
III. The grammar is suitable for bottom-up parsing.

Which of the following is true: 
A) Only I is true
B) Only II is true
C) Only III is true
D) Both II and III are true
"""

def analyze_grammar(grammar: str) -> dict:
    """
    Analyze a given context-free grammar.

    Args:
    grammar (str): A string representing the context-free grammar.
                  e.g., "S → ( S ) | x"

    Returns:
    dict: A dictionary containing the analysis results.
    """

    # Initialize analysis results
    results = {
        "ambiguous": False,
        "top_down": True,
        "bottom_up": True
    }

    # Split grammar into left and right sides
    left, right = grammar.split("→")

    # Remove leading and trailing whitespaces
    left = left.strip()
    right = right.strip()

    # Check if the grammar is ambiguous
    if "|" in right:
        # If the right side contains "|", it may be ambiguous
        results["ambiguous"] = True
    else:
        # If the right side does not contain "|", it is not ambiguous
        results["ambiguous"] = False

    # Check if the grammar is suitable for top-down parsing
    if "(" in right and ")" in right:
        # If the right side contains "(", it is suitable for top-down parsing
        results["top_down"] = True
    else:
        # If the right side does not contain "(", it is not suitable for top-down parsing
        results["top_down"] = False

    # Check if the grammar is compatible with bottom-up parsing
    if "S" in left and "(" in right and ")" in right:
        # If the left side contains "S" and the right side contains "(" and ")", it is compatible with bottom-up parsing
        results["bottom_up"] = True
    else:
        # If the left side does not contain "S" or the right side does not contain "(" and ")", it is not compatible with bottom-up parsing
        results["bottom_up"] = False

    return results