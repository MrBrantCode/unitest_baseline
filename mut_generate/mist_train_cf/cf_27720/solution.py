"""
QUESTION:
Create a function called `analyze_imports` that takes a list of import statements as strings and returns a dictionary where the keys are the package names and the values are the count of unique modules imported from each package. The function should be able to handle both `import` and `from` statements, and it should exclude any aliased module names.
"""

def analyze_imports(imported_modules):
    """
    Analyze a list of import statements and return a dictionary where the keys are the package names and the values are the count of unique modules imported from each package.

    Args:
        imported_modules (list): A list of import statements as strings.

    Returns:
        dict: A dictionary where the keys are the package names and the values are the count of unique modules imported from each package.
    """
    package_counts = {}
    for module in imported_modules:
        if 'import ' in module:
            package_name = module.split(' ')[1]
            if ' as ' in package_name:
                package_name = package_name.split(' as ')[0]
            if '.' in package_name:
                package_name = package_name.split('.')[0]
            if package_name in package_counts:
                package_counts[package_name] += 1
            else:
                package_counts[package_name] = 1

        if 'from ' in module:
            package_name = module.split(' ')[1]
            if '.' in package_name:
                package_name = package_name.split('.')[0]
            if package_name in package_counts:
                package_counts[package_name] += 1
            else:
                package_counts[package_name] = 1

    return package_counts