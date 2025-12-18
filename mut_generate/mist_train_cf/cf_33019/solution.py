"""
QUESTION:
Write a function `assignLastElement` that takes four parameters: `X_arai`, `Y_arai`, `X_IZZI_MD`, and `Y_IZZI_MD`, which are all arrays of integers. The function should assign the last element of `X_arai` to the last element of `X_IZZI_MD` and the last element of `Y_arai` to the last element of `Y_IZZI_MD`. The function should return the modified `X_IZZI_MD` and `Y_IZZI_MD` arrays. Assume that `X_arai` and `Y_arai` will always have at least one element, and their lengths will be the same as the lengths of `X_IZZI_MD` and `Y_IZZI_MD`.
"""

def assignLastElement(X_arai, Y_arai, X_IZZI_MD, Y_IZZI_MD):
    X_IZZI_MD[-1] = X_arai[-1]
    Y_IZZI_MD[-1] = Y_arai[-1]
    return X_IZZI_MD, Y_IZZI_MD