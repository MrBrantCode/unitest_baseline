"""
QUESTION:
Create a data structure to store employee records, where each employee can have multiple roles and each role can have multiple projects assigned to it. The structure should allow for easy navigation and retrieval of employee records and their associated roles and projects.
"""

class Node:
    """Represents a node in the employee records tree structure."""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.roles = []

class Role:
    """Represents a role associated with an employee."""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.projects = []

def create_employee_record(employee_id, employee_name, roles):
    """
    Creates an employee record with multiple roles and projects.

    Args:
        employee_id (int): A unique identifier for the employee.
        employee_name (str): The name of the employee.
        roles (list): A list of dictionaries containing role information.
            Each dictionary should have the following keys:
                - id (int): A unique identifier for the role.
                - name (str): The name of the role.
                - projects (list): A list of project names assigned to the role.

    Returns:
        Node: The created employee record node.
    """
    employee_node = Node(employee_id, employee_name)
    for role_info in roles:
        role = Role(role_info['id'], role_info['name'])
        role.projects = role_info['projects']
        employee_node.roles.append(role)
    return employee_node