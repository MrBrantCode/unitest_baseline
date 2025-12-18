"""
QUESTION:
Write a function `form_submission_options` that takes a URL and a submission method as input, and returns a string representing the form submission options. The function should consider the trade-offs between simplicity and flexibility in choosing the submission method, and whether to include query string parameters. 

Restrictions: The submission method should be either 'simple' or 'custom', where 'simple' represents using a helper method that generates the form elements automatically, and 'custom' represents manually writing out the form tag and setting the action and method attributes.
"""

def form_submission_options(url, submission_method):
    """
    Returns a string representing the form submission options based on the provided URL and submission method.

    Args:
        url (str): The URL for the form submission.
        submission_method (str): The submission method, either 'simple' or 'custom'.

    Returns:
        str: A string representing the form submission options.
    """

    if submission_method == 'simple':
        # Using Html.BeginForm() for simplicity and speed
        return f"Html.BeginForm('{url}')"
    
    elif submission_method == 'custom':
        # Manually writing out the form tag for more control
        return f"<form action='{url}'>"
    
    else:
        # Invalid submission method
        return "Invalid submission method. Please use 'simple' or 'custom'."