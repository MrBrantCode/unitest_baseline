"""
QUESTION:
Create a function called `get_artifact_info` that accepts the name of an artifact as an argument and returns its corresponding historical period and description. The function should be able to handle cases where the artifact does not exist.

Create a dictionary called `ancient_artifacts` with artifact names as keys and nested dictionaries containing historical periods and descriptions as values.

Implement three additional functions: `update_artifact`, `delete_artifact`, and `add_artifact`. These functions should allow updating, deleting, and adding new artifacts to the dictionary, respectively, and handle cases where the artifact does not exist.

The `update_artifact`, `delete_artifact`, and `add_artifact` functions should accept the artifact name and corresponding historical period and description as arguments.
"""

def get_artifact_info(artifact_name, ancient_artifacts):
    try:
        artifact = ancient_artifacts[artifact_name]
        return artifact
    except KeyError:
        return "This artifact does not exist in our records."

def update_artifact(artifact_name, period, description, ancient_artifacts):
    ancient_artifacts[artifact_name] = {'period': period, 'description': description}

def delete_artifact(artifact_name, ancient_artifacts):
    try:
        del ancient_artifacts[artifact_name]
    except KeyError:
        print("This artifact does not exist in our records.")

def add_artifact(artifact_name, period, description, ancient_artifacts):
    ancient_artifacts[artifact_name] = {'period': period, 'description': description}