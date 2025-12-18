"""
QUESTION:
Create a function that runs under different user credentials in a Google Apps Script project. The project has two functions related to Google Drive, where the first function should run with the credentials of the user accessing the app, and the second function should run under the credentials of the admin without sharing the admin credentials with the end user. The function should adhere to Google Apps Script's security restrictions.
"""

def run_under_different_credentials(function, user_type):
    """
    Simulate running a function under different user credentials in a Google Apps Script project.

    Args:
        function (str): The function to be executed.
        user_type (str): The type of user ('user' or 'admin').

    Returns:
        str: A message indicating the function execution under the specified user type.
    """
    if user_type == 'user':
        # Run the function as the user accessing the app
        return f"Running {function} as the user..."
    elif user_type == 'admin':
        # Run the function as the admin (using service account or OAuth2)
        return f"Running {function} as the admin..."
    else:
        return "Invalid user type. Please specify 'user' or 'admin'."

# Example usage (Note: This will not actually run the function, but just demonstrate the function signature)
# print(run_under_different_credentials('my_function', 'user'))
# print(run_under_different_credentials('my_function', 'admin'))