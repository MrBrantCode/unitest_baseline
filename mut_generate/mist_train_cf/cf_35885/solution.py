"""
QUESTION:
Implement a function `selectOptimalSpar` that takes in a set of candidate smoothing parameters `sparSet`, input data `x` and `y`, a scale parameter `sc`, and additional parameters `pars`, and returns the optimal smoothing parameter based on the cross-validated prediction error. The function should use a helper function `R_runmed_spline_KCV_predErr` to calculate the cross-validated prediction error for each candidate smoothing parameter. If there are multiple parameters with the same minimum prediction error, the function should select the smoothest one (i.e., the last one in the array). The `R_runmed_spline_KCV_predErr` function is not provided and should be implemented separately.
"""

def selectOptimalSpar(sparSet, x, y, sc, **pars):
    predErrSet = [R_runmed_spline_KCV_predErr(x, y, spar=spar, sc=sc, **pars) for spar in sparSet]
    min_pred_err = min(predErrSet)
    min_pred_spar_indices = [i for i, err in enumerate(predErrSet) if err == min_pred_err]
    spar = sparSet[min_pred_spar_indices[-1]] 
    return spar