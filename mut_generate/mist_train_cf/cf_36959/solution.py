"""
QUESTION:
Implement a function `filter_projects(projects, filters)` that filters a list of projects based on certain criteria. The `projects` parameter is a list of dictionaries, where each dictionary represents a project with attributes. The `filters` parameter is a set of strings representing the criteria for filtering the projects. Each filter string should be in the format 'key:value' or '-key:value', where '-' denotes exclusion. The function should filter the projects based on the following criteria: include projects that match the filter if the filter does not start with '-', and exclude projects that match the filter if it starts with '-'. Return the filtered list of projects.
"""

def filter_projects(projects, filters):
    filtered_projects = projects.copy()

    for f in filters:
        exclude = False
        if f.startswith('-'):
            exclude = True
            f = f[1:]

        key, value = f.split(':')
        filtered_projects = [p for p in filtered_projects if (p.get(key) == value) != exclude]

    return filtered_projects