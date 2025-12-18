"""
QUESTION:
Create a function `profile_table` that returns a string representation of an HTML table containing a user's profile information. The table should have a header row with the columns 'Full Name', 'Username', 'Email', and 'Phone', and a data row with the corresponding user information. The function will be passed a dictionary object `user` containing the user's profile information with keys 'full_name', 'username', 'email', and 'phone'.
"""

def profile_table(user):
    """
    Returns a string representation of an HTML table containing a user's profile information.

    Args:
        user (dict): A dictionary object containing the user's profile information.
            It should have keys 'full_name', 'username', 'email', and 'phone'.

    Returns:
        str: A string representation of an HTML table containing the user's profile information.
    """
    return """
    <table>
      <tr>
        <th>Full Name</th>
        <th>Username</th>
        <th>Email</th>
        <th>Phone</th>
      </tr>
      <tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
      </tr>
    </table>
    """.format(user['full_name'], user['username'], user['email'], user['phone'])