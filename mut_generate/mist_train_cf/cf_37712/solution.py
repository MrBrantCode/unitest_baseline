"""
QUESTION:
Implement the `apply_lang` function, which takes in a list of text lines and a state object. The function should apply language-specific transformations to the text lines based on the state. The state object contains `keywords`, `operators`, and `indentation` properties. The function should replace all occurrences of keywords with uppercase versions, replace all occurrences of operators with bolded versions, and indent each line by the number of spaces specified in the `indentation` property. The function should return the transformed text lines as a list.
"""

def apply_lang(text_lines, state):
    """
    Applies language-specific transformations to the text lines based on the state.

    Args:
    text_lines (list): A list of text lines.
    state (dict): A state object containing 'keywords', 'operators', and 'indentation' properties.

    Returns:
    list: The transformed text lines.
    """
    output = []
    for line in text_lines:
        for keyword in state["keywords"]:
            line = line.replace(keyword, keyword.upper())
        for operator in state["operators"]:
            line = line.replace(operator, f'**{operator}**')
        line = " " * state["indentation"] + line
        output.append(line)
    return output