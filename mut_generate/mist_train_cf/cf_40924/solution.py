"""
QUESTION:
Write a Python function `process_parameters` that takes 11 input parameters and returns a dictionary containing the settings for a data processing pipeline. The function should handle the conditional logic based on the variables and return the appropriate settings.

The function signature should be: 
`def process_parameters(save_dir, save_stem, experiments_fn, source_acronyms, solver, fit_gaussian, select_one_lambda, cross_val, save_mtx, cross_val_matrices, selected_fit_cmds, cmdfile):`

The function should return a dictionary with the following keys: 'save_dir', 'experiments_fn', 'target_acronyms', 'solver', 'cmdfile', 'selected_fit_cmds', 'save_mtx', 'cross_val_matrices', 'cross_val', 'fit_gaussian', 'select_one_lambda'. 

Note that 'save_dir' should be a path created by joining the input 'save_dir' with 'save_stem', and 'solver' should be an absolute path. The paths for 'cmdfile' and 'selected_fit_cmds' should be created by joining the 'save_dir' with 'model_fitting_cmds' and 'model_fitting_after_selection_cmds', respectively.
"""

import os

def process_parameters(save_dir, save_stem, experiments_fn, source_acronyms, solver, fit_gaussian, select_one_lambda, cross_val, save_mtx, cross_val_matrices, selected_fit_cmds, cmdfile):
    settings = {
        'save_dir': os.path.join(save_dir, save_stem),
        'experiments_fn': experiments_fn,
        'target_acronyms': source_acronyms,
        'solver': os.path.abspath(solver),
        'cmdfile': os.path.join(os.path.join(save_dir, save_stem), 'model_fitting_cmds'),
        'selected_fit_cmds': os.path.join(os.path.join(save_dir, save_stem), 'model_fitting_after_selection_cmds'),
        'save_mtx': save_mtx,
        'cross_val_matrices': cross_val_matrices,
        'cross_val': cross_val,
        'fit_gaussian': fit_gaussian,
        'select_one_lambda': select_one_lambda
    }

    return settings