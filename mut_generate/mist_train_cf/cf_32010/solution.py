"""
QUESTION:
Implement a `CustomTransformer` class with a `transform` method that takes input data `X` and returns the transformed data. The transformation should subtract the values of the `variables` from the corresponding values of the `related_variable` in the input data `X`. The `variables` and `related_variable` are attributes of the `CustomTransformer` class. Do not modify the original input data `X`.
"""

def custom_transformer_transform(X, variables, related_variable):
    X = X.copy()
    for variable in variables:
        X[variable] = X[related_variable] - X[variable]
    return X