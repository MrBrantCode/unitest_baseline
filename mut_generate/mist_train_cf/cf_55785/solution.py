"""
QUESTION:
Implement a custom login and user role system in CruiseControl.NET's dashboard, allowing certain individuals to force a build on a per project basis. The dashboard uses the nVelocity view engine. The solution should include authentication and authorization, allowing specific users or roles to perform certain actions. Please provide a solution that can be implemented either by modifying the existing nVelocity code or by using a combination of nVelocity and other technologies.
"""

def login_and_authorize_user(username, password, project_name):
    """
    Custom login and user role system in CruiseControl.NET's dashboard.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.
        project_name (str): The name of the project.

    Returns:
        bool: True if the user is authorized to force a build on the project, False otherwise.
    """

    # Assuming we have a dictionary of users and their roles
    users = {
        "user1": {"password": "password1", "roles": ["admin"]},
        "user2": {"password": "password2", "roles": ["developer"]},
    }

    # Assuming we have a dictionary of projects and their authorized roles
    projects = {
        "project1": ["admin"],
        "project2": ["admin", "developer"],
    }

    # Check if the user exists and the password is correct
    if username in users and users[username]["password"] == password:
        # Check if the user has the required role for the project
        if project_name in projects and any(role in users[username]["roles"] for role in projects[project_name]):
            return True

    return False