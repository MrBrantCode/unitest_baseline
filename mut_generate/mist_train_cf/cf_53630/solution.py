"""
QUESTION:
Write a function `add_script_to_evaluate` that takes a string `os` as input and returns a dictionary with the key "source" containing a string representing JavaScript code. The JavaScript code should define a getter for `navigator.platform` that returns the value of `os`. The function should use string formatting to insert the value of `os` into the JavaScript code.

Restrictions:
- The JavaScript code should be a string.
- The value of `os` should be inserted into the JavaScript code using Python string formatting.
- The function should return a dictionary with a single key "source" containing the JavaScript code as a string.
"""

def add_script_to_evaluate(os):
    """
    Returns a dictionary with the key "source" containing a string representing JavaScript code.
    The JavaScript code defines a getter for `navigator.platform` that returns the value of `os`.

    Args:
        os (str): The value to be returned by the `navigator.platform` getter.

    Returns:
        dict: A dictionary with a single key "source" containing the JavaScript code as a string.
    """

    return {
        "source": f"""
            Object.defineProperty(navigator, 'platform', {{get: () => "{os}"}})
        """
    }