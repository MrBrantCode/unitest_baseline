"""
QUESTION:
Create a function `get_module_descriptions` that takes a list of Gallagher Access Control Hardware Module types as input and returns a dictionary where the keys are the module types and the values are their corresponding descriptions. The function should include descriptions for the following module types: "Controller", "Reader", "Input/Output", "Door", "Locks", "Power", "Communication", and "cModules".
"""

def get_module_descriptions(modules):
    module_types = {
        "Controller": "A device that manages and controls access to a set of doors.",
        "Reader": "A device that reads credentials (such as cards or fingerprints) to grant or deny access.",
        "Input/Output": "A device that provides input/output functionality, such as allowing users to request access or triggering alarms.",
        "Door": "A physical barrier that can be controlled by an access control system.",
        "Locks": "A device that can be used to lock or unlock a door.",
        "Power": "A device that supplies power to other hardware modules in the access control system.",
        "Communication": "A device that allows the access control system to communicate with other systems or devices.",
        "cModules": "Custom hardware modules developed by Gallagher for specific access control scenarios."
    }
    
    return {module: module_types.get(module) for module in modules}