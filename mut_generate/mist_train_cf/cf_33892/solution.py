"""
QUESTION:
Create a function `common_requirements(package_dependencies)` that takes a dictionary `package_dependencies` as input. The dictionary has two keys: `install_requires` and `extras_require`. The `install_requires` key maps to a list of strings representing packages, while the `extras_require` key maps to a dictionary with keys like `dev` and `docs` that map to lists of strings representing additional packages. The function should return a list of unique packages that are common to both `dev` and `docs` lists under `extras_require`. If either `dev` or `docs` is missing, return an empty list or a list of common packages with the existing key.
"""

def common_requirements(package_dependencies):
    dev_requirements = set(package_dependencies.get("extras_require", {}).get("dev", []))
    docs_requirements = set(package_dependencies.get("extras_require", {}).get("docs", []))
    
    common_packages = list(dev_requirements.intersection(docs_requirements))
    return common_packages