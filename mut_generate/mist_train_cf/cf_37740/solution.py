"""
QUESTION:
Implement a function `format_search_results` that formats the left and right fragments of text for displaying search results, adhering to the specified maximum character limits and including ellipses where necessary. The function takes in the following parameters:
- `left`: A list of words representing the left fragment of text.
- `right`: A list of words representing the right fragment of text.
- `num_right_words`: An integer representing the number of words allowed in the right fragment.
- `MAX_NUM_CHAR_FRAGMENT`: An integer representing the maximum number of characters allowed for each fragment.
- `ELLIPSIS`: A constant string representing the ellipsis ("...").
- `color`: A constant representing the color for the matched text.

The function should return a tuple containing the formatted left and right fragments and the assigned color for the matched text.
"""

def format_search_results(left, right, num_right_words, MAX_NUM_CHAR_FRAGMENT, ELLIPSIS, color):
    """
    Formats the left and right fragments of text for displaying search results.

    Args:
        left (list): A list of words representing the left fragment of text.
        right (list): A list of words representing the right fragment of text.
        num_right_words (int): An integer representing the number of words allowed in the right fragment.
        MAX_NUM_CHAR_FRAGMENT (int): An integer representing the maximum number of characters allowed for each fragment.
        ELLIPSIS (str): A constant string representing the ellipsis ("...").
        color (str): A constant representing the color for the matched text.

    Returns:
        tuple: A tuple containing the formatted left and right fragments and the assigned color for the matched text.
    """

    # Ensure the right fragment has the required number of words
    if len(right) < num_right_words:
        right = right + [ELLIPSIS]

    # Join the left and right fragments into strings
    left = ' '.join(left)
    right = ' '.join(right)

    # Truncate the left fragment if it exceeds the maximum character limit
    if len(left) > MAX_NUM_CHAR_FRAGMENT:
        left = ELLIPSIS + left[-(MAX_NUM_CHAR_FRAGMENT-3):]  # Include space for the ellipsis

    # Truncate the right fragment if it exceeds the maximum character limit
    if len(right) > MAX_NUM_CHAR_FRAGMENT:
        right = right[:MAX_NUM_CHAR_FRAGMENT-3] + ELLIPSIS  # Include space for the ellipsis

    # Assign the color for the matched text
    match_color = color

    return left, right, match_color