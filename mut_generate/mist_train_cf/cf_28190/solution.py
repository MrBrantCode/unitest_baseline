"""
QUESTION:
Create a function `register_workflow` that takes `workflow_name`, `settings`, `logger`, and `conn` as input parameters. The function should dynamically import a module named `workflow_<workflow_name>`, instantiate an object of the class with the same name, and then register the workflow. The function should return the response from the registration.
"""

import importlib

def register_workflow(workflow_name, settings, logger, conn):
    class_name = "workflow_" + workflow_name
    module_name = "workflow." + class_name
    imported_module = importlib.import_module(module_name)
    workflow_class = getattr(imported_module, class_name)
    workflow_object = workflow_class(settings, logger, conn)
    response = workflow_object.register()
    return response