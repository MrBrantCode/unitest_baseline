"""
QUESTION:
Write a function `best_window_size` that takes the original time series data and the reconstructed time series for different window sizes as input and returns the window size that produces the most accurate reconstruction of the original time series. The function should take five parameters: `orig_TS` and four reconstructed time series, each corresponding to a specific window size (8, 9, 10, and 11). The function should return the window size that produces the smallest mean squared error between the original time series and the reconstructed time series. Assume that the length of `orig_TS` is the same as the lengths of the reconstructed time series.
"""

def best_window_size(orig_TS, F8, F9, F10, F11):
    def mean_squared_error(true, pred):
        return sum((t - p) ** 2 for t, p in zip(true, pred)) / len(true)

    errors = {
        8: mean_squared_error(orig_TS, F8),
        9: mean_squared_error(orig_TS, F9),
        10: mean_squared_error(orig_TS, F10),
        11: mean_squared_error(orig_TS, F11)
    }

    best_window = min(errors, key=errors.get)
    return best_window