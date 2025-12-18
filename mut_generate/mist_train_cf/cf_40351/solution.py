"""
QUESTION:
Create a function called `process_yaml_data` that takes a dictionary containing YAML data as input and returns a dictionary report. The input dictionary is expected to have a 'roles' key containing a dictionary of roles with their corresponding values. The output report should have the keys 'name', 'changes', 'result', 'comment', and 'comments', where 'name' is the name of the roles, 'changes' contains any changes made, 'result' indicates the overall result, 'comment' provides any additional comments, and 'comments' contains a list of comments.
"""

def process_yaml_data(yaml_data: dict) -> dict:
    report = {'name': '',
              'changes': {},
              'result': True,
              'comment': '',
              'comments': []}

    if 'roles' in yaml_data:
        for role, values in yaml_data['roles'].items():
            report['name'] = role
            # Process the absent roles and generate the report
            # For simplicity, assuming no changes and a successful result
            report['changes'] = {}
            report['result'] = True
            report['comment'] = 'Roles processed successfully'
            report['comments'] = []

    return report