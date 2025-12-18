"""
QUESTION:
Write a function `organizational_hierarchy(json_data)` that takes a JSON object representing a company's organizational structure as input and returns a hierarchical representation of the organizational structure in the form of nested dictionaries. The JSON object contains employees and their respective managers, with each employee having a unique ID, a name, and a manager ID. The manager ID refers to the ID of the employee's direct manager, and the top-level manager has a manager ID of null. The output should include the employee's ID, name, manager ID, and a list of their direct reports, which are also represented as nested dictionaries.
"""

def organizational_hierarchy(json_data):
    employees = {emp["id"]: emp for emp in json_data["employees"]}
    top_manager = next(emp for emp in json_data["employees"] if emp["managerId"] is None)

    def build_hierarchy(employee_id):
        employee = employees[employee_id]
        return {
            "id": employee["id"],
            "name": employee["name"],
            "managerId": employee["managerId"],
            "directReports": [build_hierarchy(emp["id"]) for emp in json_data["employees"] if emp["managerId"] == employee["id"]]
        }

    return build_hierarchy(top_manager["id"])