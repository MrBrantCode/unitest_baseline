"""
QUESTION:
Implement the `calc_cliff_rmse` method to calculate the root mean square error (RMSE) for different types of compounds using various comparison methods. The method should accept the reference values, predicted values, and the following types of compounds as input: `tanimoto_cliff_compounds`, `scaffold_cliff_compounds`, `levenshtein_cliff_compounds`, and `soft_consensus_cliff_compounds`. The method should return a dictionary containing the RMSE for each type of compound. If any of the compound comparison inputs are not provided, the method should handle this case accordingly.
"""

import numpy as np

def calc_cliff_rmse(reference, predictions, tanimoto_cliff_compounds=None,
                    scaffold_cliff_compounds=None, levenshtein_cliff_compounds=None,
                    soft_consensus_cliff_compounds=None):
    """
    Calculate the root mean square error (RMSE) for different types of compounds.

    Args:
    - reference (list): Reference values.
    - predictions (list): Predicted values.
    - tanimoto_cliff_compounds (list, optional): Tanimoto cliff compounds. Defaults to None.
    - scaffold_cliff_compounds (list, optional): Scaffold cliff compounds. Defaults to None.
    - levenshtein_cliff_compounds (list, optional): Levenshtein cliff compounds. Defaults to None.
    - soft_consensus_cliff_compounds (list, optional): Soft consensus cliff compounds. Defaults to None.

    Returns:
    - dict: A dictionary containing the RMSE for each type of compound.
    """

    rmse_results = {}

    if tanimoto_cliff_compounds is not None:
        tanimoto_rmse = np.sqrt(np.mean((reference[tanimoto_cliff_compounds] - predictions[tanimoto_cliff_compounds]) ** 2))
        rmse_results['tanimoto'] = tanimoto_rmse

    if scaffold_cliff_compounds is not None:
        scaffold_rmse = np.sqrt(np.mean((reference[scaffold_cliff_compounds] - predictions[scaffold_cliff_compounds]) ** 2))
        rmse_results['scaffold'] = scaffold_rmse

    if levenshtein_cliff_compounds is not None:
        levenshtein_rmse = np.sqrt(np.mean((reference[levenshtein_cliff_compounds] - predictions[levenshtein_cliff_compounds]) ** 2))
        rmse_results['levenshtein'] = levenshtein_rmse

    if soft_consensus_cliff_compounds is not None:
        soft_consensus_rmse = np.sqrt(np.mean((reference[soft_consensus_cliff_compounds] - predictions[soft_consensus_cliff_compounds]) ** 2))
        rmse_results['soft_consensus'] = soft_consensus_rmse

    return rmse_results