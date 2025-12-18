"""
QUESTION:
Write a function `analyze_coefficients` that takes a cross-validated model `cv_model` as input and returns the average and standard deviation of the coefficients across all the estimators. The `cv_model` is a dictionary containing multiple estimators and their coefficients.

The function should return a tuple containing two lists: the first list contains the average coefficients for each feature across all estimators, and the second list contains the standard deviation of coefficients for each feature across all estimators.

The input `cv_model` has the following structure:
- `cv_model` (dict): A dictionary with a key "estimator" containing a list of dictionaries.
- Each dictionary in the list represents an estimator and has a key "transformedtargetregressor" with a nested dictionary.
- The nested dictionary has a key "regressor_" with a nested dictionary containing a key "coef_" with a list of coefficients.

Example:
```python
cv_model = {
    "estimator": [
        {"transformedtargetregressor": {"regressor_": {"coef_": [0.5, 0.3, 0.2]}}},
        {"transformedtargetregressor": {"regressor_": {"coef_": [0.4, 0.2, 0.1]}}},
        {"transformedtargetregressor": {"regressor_": {"coef_": [0.6, 0.4, 0.3]}}}
    ]
}
```
"""

import numpy as np

def analyze_coefficients(cv_model: dict) -> (list, list):
    coefficients = [est["transformedtargetregressor"]["regressor_"]["coef_"] for est in cv_model["estimator"]]
    average_coeffs = np.mean(coefficients, axis=0)
    std_coeffs = np.std(coefficients, axis=0)
    return average_coeffs.tolist(), std_coeffs.tolist()