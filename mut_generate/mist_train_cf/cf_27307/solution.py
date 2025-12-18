"""
QUESTION:
Configure the solvers for two different model parts based on the provided project parameters. The function should take in the project parameters for the background and boundary-fitted model parts (`project_parameters_BG` and `project_parameters_BF`) and the corresponding model parts (`main_model_part_bg` and `main_model_part_bf`). The function should create solvers for each model part using the specified solver type from the project parameters, add the required variables to the solvers, and return the configured solvers. 

The function signature is `def configure_solvers(project_parameters_BG, project_parameters_BF, main_model_part_bg, main_model_part_bf):`. 

The `project_parameters_BG` and `project_parameters_BF` are dictionaries containing the project parameters, including the solver type. The `main_model_part_bg` and `main_model_part_bf` are the model parts for the background and boundary-fitted domains.
"""

def configure_solvers(project_parameters_BG, project_parameters_BF, main_model_part_bg, main_model_part_bf):
    # Solver construction for background model part
    solver_module_bg = __import__(project_parameters_BG["solver_settings"]["solver_type"].GetString())
    solver_bg = solver_module_bg.CreateSolver(main_model_part_bg, project_parameters_BG["solver_settings"])
    solver_bg.AddVariables()

    # Solver construction for boundary-fitted model part
    solver_module_bf = __import__(project_parameters_BF["solver_settings"]["solver_type"].GetString())
    solver_bf = solver_module_bf.CreateSolver(main_model_part_bf, project_parameters_BF["solver_settings"])
    solver_bf.AddVariables()

    # Additional configuration or operations if needed
    # ...

    return solver_bg, solver_bf  # Return the configured solvers for both model parts